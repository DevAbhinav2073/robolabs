from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from main.api_calls import get_invoices
from main.forms import FilterForm
from django.template.response import TemplateResponse


class InvoiceTableView(TemplateView):
    template_name = "main/table.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        from_date = '2022-01-01'
        to_date = '2022-01-31'
        if self.request.method == 'POST':
            from_date = self.request.POST.get('from_date')
            to_date = self.request.POST.get('to_date')
        records = get_invoices(from_date, to_date)
        ctx.update(
            {
                'records': records,
                'form': FilterForm(initial={
                    'from_date': from_date,
                    'to_date': to_date
                }),
                'from_date': from_date,
                'to_date': to_date,
                'records_count': len(records)
            }
        )
        return ctx

    def post(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        return TemplateResponse(request, 'main/table.html', context=ctx)
