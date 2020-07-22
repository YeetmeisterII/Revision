from functools import lru_cache

from pages.code.pages.context_processing import local_link_converter


@lru_cache
def links():
    context = [
        {
            'topic_name': 'Business',
            'link_data':
                [
                    {'name': 'Index', 'viewname': 'business:index'},
                    {'name': 'Glossary', 'viewname': 'business:glossary'},
                ]
        },
        {
            'topic_name': 'Marketing and People',
            'link_data': [
                {'name': 'Meeting Customer Needs', 'viewname': 'business:topic_page',
                 'args': ['marketing_and_people', 'meeting_customer_needs']},
                {'name': 'Market', 'viewname': 'business:topic_page', 'args': ['marketing_and_people', 'market']},
                {'name': 'Marketing Mix and Strategy', 'viewname': 'business:topic_page',
                 'args': ['marketing_and_people', 'marketing_mix_and_strategy']},
                {'name': 'Managing People', 'viewname': 'business:topic_page',
                 'args': ['marketing_and_people', 'managing_people']},
                {'name': 'Entrepreneurs and Leaders', 'viewname': 'business:topic_page',
                 'args': ['marketing_and_people', 'entrepreneurs_and_leaders']},
            ]
        },
        {
            'topic_name': 'Managing Business Activity',
            'link_data': [
                {'name': 'Raising Finance', 'viewname': 'business:topic_page',
                 'args': ['managing_business_activity', 'raising_finance']},
                {'name': 'Financial Planning', 'viewname': 'business:topic_page',
                 'args': ['managing_business_activity', 'financial_planning']},
                {'name': 'Managing Finance', 'viewname': 'business:topic_page',
                 'args': ['managing_business_activity', 'managing_finance']},
                {'name': 'Resource Management', 'viewname': 'business:topic_page',
                 'args': ['managing_business_activity', 'resource_management']},
                {'name': 'External Influences', 'viewname': 'business:topic_page',
                 'args': ['managing_business_activity', 'external_influences']},
            ]
        },
        {
            'topic_name': 'Business Decisions and Strategy',
            'link_data': [
                {'name': 'Business Objectives and Strategy', 'viewname': 'business:topic_page',
                 'args': ['business_decisions_and_strategy', 'business_objectives_and_strategy']},
                {'name': 'Business Growth', 'viewname': 'business:topic_page',
                 'args': ['business_decisions_and_strategy', 'business_growth']},
                {'name': 'Decision-Making Techniques', 'viewname': 'business:topic_page',
                 'args': ['business_decisions_and_strategy', 'decisionmaking_techniques']},
                {'name': 'Influences on Business Decisions', 'viewname': 'business:topic_page',
                 'args': ['business_decisions_and_strategy', 'influences_on_business_decisions']},
                {'name': 'Assessing Competitiveness', 'viewname': 'business:topic_page',
                 'args': ['business_decisions_and_strategy', 'assessing_competitiveness']},
                {'name': 'Assessing Competitiveness', 'viewname': 'business:topic_page',
                 'args': ['business_decisions_and_strategy', 'assessing_competitiveness']},
                {'name': 'Managing Change', 'viewname': 'business:topic_page',
                 'args': ['business_decisions_and_strategy', 'managing_change']},
            ]
        },
        {
            'topic_name': 'Global Business',
            'link_data': [
                {'name': 'Globalisation', 'viewname': 'business:topic_page',
                 'args': ['global_business', 'globalisation']},
                {'name': 'Global Markets and Business Expansion', 'viewname': 'business:topic_page',
                 'args': ['global_business', 'global_markets_and_business_expansion']},
                {'name': 'Global Marketing', 'viewname': 'business:topic_page',
                 'args': ['global_business', 'global_marketing']},
                {'name': 'Global Industries and Companies', 'viewname': 'business:topic_page',
                 'args': ['global_business', 'global_industries_and_companies']},
            ]
        },
    ]
    return {'business_links': local_link_converter(context)}


def business_links(request):
    return links()
