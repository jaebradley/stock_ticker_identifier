from publicly_traded_companies.view_sets import ExchangeViewSet

exchanges_list = ExchangeViewSet.as_view({
    'get': 'list'
})

exchange_detail = ExchangeViewSet.as_view({
    'get': 'retrieve'
})
