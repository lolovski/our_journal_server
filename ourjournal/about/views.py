from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class AboutSupportView(TemplateView):
    template_name = 'about/support.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class AboutFAQView(TemplateView):
    template_name = 'about/FAQ.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class AboutChatBotView(TemplateView):
    template_name = 'about/chat_bot_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

