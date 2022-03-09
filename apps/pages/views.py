from django.views.generic import TemplateView
from apps.match.models import Match
from datetime import datetime, timedelta


class LandingTemplateView(TemplateView):
    template_name = "pages/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['report'] = {

            "data": self.data_match_board()
            # "last_fetch_stat": AccSMSFetchStat.objects.last().fetch_datetime
        }

        return self.render_to_response(context)

    def data_match_board(self):

        now = datetime.now().date()

        title_unique = Match.objects.filter(date__date=now).values('title').distinct()

        array_match_board = []

        for item in title_unique:

            # print(item)

            array_match = []

            data = {
                "header": item['title'],
                "body": array_match
            }

            list_links = Match.objects.filter(date__date=now, title=item['title']).values(
                'live_link__link',
                'live_link__type',
                'live_link__logo'

            )

            list_body = Match.objects.filter(date__date=now, title=item['title']).values(
                'date',
                'title',
                'home_team__id',
                'away_team__id',
                'home_team__name',
                'home_team__logo',
                'away_team__name',
                'away_team__logo',
            )

            # array_links = []

            if len(list_body) != 0:

                for item_body in list_body:

                    array_links = []

                    list_links = Match.objects.filter(date__date=now, title=item_body['title'], home_team__id=item_body['home_team__id'], away_team__id=item_body['away_team__id']).values(
                        'live_link__link',
                        'live_link__type',
                        'live_link__logo'

                    )

                    for item_link in list_links:

                        link = item_link['live_link__link']
                        link_type = item_link['live_link__type']
                        link_logo = item_link['live_link__logo']

                        datas_l = {
                            "link": link,
                            "type": link_type,
                            'logo': link_logo
                        }

                        array_links.append(datas_l)

                    dates = {
                        "date": (item_body['date'] + timedelta(hours=7)).strftime("%Y-%m-%d"),
                        "time": (item_body['date'] + timedelta(hours=7)).strftime("%H:%M"),
                        "title": item_body['title'],
                        "home_team__name": item_body['home_team__name'],
                        "home_team__logo": item_body['home_team__logo'],
                        "away_team__name": item_body['away_team__name'],
                        "away_team__logo": item_body['away_team__logo'],
                        "link_live": array_links

                    }


                    array_match.append(dates)

            array_match_board.append(data)

        if array_match_board == []:
            data = 0
        else:
            data = array_match_board

        return data


class LiveStreamLandingTemplateView(TemplateView):

    #template_name = "pages/live_stream_landing.html"
    template_name = "pages/live_stream_landing.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['report'] = {

            "data": []
        }

        return self.render_to_response(context)
