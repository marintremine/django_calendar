from django.shortcuts import render
from calendar import HTMLCalendar
from datetime import datetime
from django.views.generic import TemplateView

class CalendarView(TemplateView):
    template_name = 'calendarapp/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Créer un objet Calendrier HTML
        cal = HTMLCalendar()

        # Obtenir le mois et l'année courants
        today = datetime.now()
        month = today.month
        year = today.year

        # Générer le calendrier HTML
        html_calendar = cal.formatmonth(year, month)

        context['calendar'] = html_calendar
        return context
