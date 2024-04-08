from django.db import transaction

from envdata.models import Company, Fuel
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from openpyxl import load_workbook
from envdata.forms import ExcelUploadForm


class ExcelUploadView(FormView):
    form_class = ExcelUploadForm
    template_name = 'envdata/upload_excel/upload_fuel_data.html'
    success_url = reverse_lazy('fuel_emissions')

    def form_valid(self, form):
        excel_file = form.cleaned_data['excel_file']
        wb = load_workbook(filename=excel_file)
        ws = wb.active

        with transaction.atomic():  # Use a transaction to ensure data integrity
            for row in ws.iter_rows(min_row=2, values_only=True):
                company_name = row[0]  # Make sure this is the correct index for company name
                if company_name:  # Check if company_name is not empty
                    company, created = Company.objects.get_or_create(name=company_name)
                    Fuel.objects.create(
                        company=company,
                        month=row[1],
                        year=row[2],
                        emission_type=row[3],
                        emission_scope=row[4],
                        fuel_type=row[5],
                        fuel_source=row[6],
                        fuel_quantity=row[7],
                        pollution_norm=row[8],
                        activity_type=row[9],
                        vehicle_type=row[10],
                        measure_unit=row[11],
                        emission_factor=row[12]
                    )
                else:
                    # Handle the case where company name is empty
                    # Maybe raise a validation error or skip this row
                    pass

        return super().form_valid(form)
