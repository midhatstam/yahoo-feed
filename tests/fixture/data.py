from dateutil import parser

success_data = {
    'bozo': False,
    'entries': [{
        'summary': "(Bloomberg) -- Microsoft Corp. unveiled a new way to purchase its flagship Windows operating system, delivering the software via the cloud from the company’s data centers to users' personal computers or tablets.The cloud-based product, called Windows 365, frees companies and users from having to install Windows and their various apps, data and settings on every computer. It will be a good choice for employees working from home, as well as interns or contractors who need a fast and temporary setu",
        'summary_detail': {
            'type': 'text/html',
            'language': None,
            'base': 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US',
            'value': "(Bloomberg) -- Microsoft Corp. unveiled a new way to purchase its flagship Windows operating system, delivering the software via the cloud from the company’s data centers to users' personal computers or tablets.The cloud-based product, called Windows 365, frees companies and users from having to install Windows and their various apps, data and settings on every computer. It will be a good choice for employees working from home, as well as interns or contractors who need a fast and temporary setu"
        },
        'id': '9abee448-251d-34ca-a9e3-8d7a66d01d24',
        'guidislink': False,
        'links': [{
            'rel': 'alternate',
            'type': 'text/html',
            'href': 'https://finance.yahoo.com/news/microsoft-readies-cloud-version-windows-150009120.html?.tsrc=rss'
        }],
        'link': 'https://finance.yahoo.com/news/microsoft-readies-cloud-version-windows-150009120.html?.tsrc=rss',
        'published': 'Wed, 14 Jul 2021 16:55:21 +0000',
        'published_parsed': parser.parse('Wed, 14 Jul 2021 16:55:21 +0000').timetuple(),
        'title': 'Microsoft Readies Cloud\xa0Version of Windows for Remote Workers',
        'title_detail': {
            'type': 'text/plain',
            'language': None,
            'base': 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US',
            'value': 'Microsoft Readies Cloud\xa0Version of Windows for Remote Workers'
        }
    }],
    'feed': {
        'rights': 'Copyright (c) 2021 Verizon Media. All rights reserved.',
        'rights_detail': {
            'type': 'text/plain',
            'language': None,
            'base': 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US',
            'value': 'Copyright (c) 2021 Verizon Media. All rights reserved.'},
        'subtitle': 'Latest Financial News for AAPL',
        'subtitle_detail': {
            'type': 'text/html',
            'language': None,
            'base': 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US',
            'value': 'Latest Financial News for AAPL'},
        'image': {
            'height': 45,
            'links': [{
                'rel': 'alternate',
                'type': 'text/html',
                'href': 'http://finance.yahoo.com/q/h?s=AAPL'
            }],
            'link': 'http://finance.yahoo.com/q/h?s=AAPL',
            'title': 'Yahoo! Finance: AAPL News',
            'title_detail': {
                'type': 'text/plain',
                'language': None,
                'base': 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US',
                'value': 'Yahoo! Finance: AAPL News'},
            'href': 'https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png',
            'width': 144
        },
        'language': 'en-US',
        'updated': 'Wed, 14 Jul 2021 17:45:50 +0000',
        'updated_parsed': parser.parse('Wed, 14 Jul 2021 17:45:50 +0000').timetuple(),
        'links': [
            {
                'rel': 'alternate',
                'type': 'text/html',
                'href': 'http://finance.yahoo.com/q/h?s=AAPL'
            }],
        'link': 'http://finance.yahoo.com/q/h?s=AAPL',
        'title': 'Yahoo! Finance: AAPL News',
        'title_detail': {
            'type': 'text/plain',
            'language': None,
            'base': 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US',
            'value': 'Yahoo! Finance: AAPL News'
        }},
    'headers': {
        'x-yahoo-request-id': 'fi3hrlhgeu8me',
        'vary': 'Origin',
        'cache-control': 'public, max-age=300, stale-while-revalidate=75',
        'content-type': 'application/xml',
        'content-encoding': 'gzip',
        'content-length': '5382',
        'x-envoy-upstream-service-time': '7',
        'date': 'Wed, 14 Jul 2021 17:45:50 GMT',
        'server': 'ATS',
        'x-envoy-decorator-operation': 'finance-newsfeed--production-ir2.finance-k8s.svc.yahoo.local:4080/*',
        'age': '0',
        'connection': 'close',
        'strict-transport-security': 'max-age=31536000',
        'expect-ct': 'max-age=31536000, report-uri="http://csp.yahoo.com/beacon/csp?src=yahoocom-expect-ct-report-only"',
        'referrer-policy': 'no-referrer-when-downgrade',
        'x-content-type-options': 'nosniff',
        'x-xss-protection': '1; mode=block',
        'x-frame-options': 'SAMEORIGIN'
    },
    'href': 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US',
    'status': 200,
    'encoding': 'utf-8',
    'version': 'rss20',
    'namespaces': {}
}

error_data = {
    'bozo': 1,
    'entries': [],
    'feed': {},
    'headers': {
        'x-yahoo-request-id': 'd606pitgeuc23',
        'content-encoding': 'gzip',
        'content-length': '58',
        'x-envoy-upstream-service-time': '0',
        'date': 'Wed, 14 Jul 2021 18:43:15 GMT',
        'server': 'ATS',
        'x-envoy-decorator-operation': 'finance-newsfeed--production-ir2.finance-k8s.svc.yahoo.local:4080/*',
        'cache-control': 'max-age=0, private',
        'expires': '-1',
        'age': '0',
        'connection': 'close',
        'strict-transport-security': 'max-age=31536000',
        'expect-ct': 'max-age=31536000, report-uri="http://csp.yahoo.com/beacon/csp?src=yahoocom-expect-ct-report-only"',
        'referrer-policy': 'no-referrer-when-downgrade',
        'x-content-type-options': 'nosniff',
        'x-xss-protection': '1; mode=block',
        'x-frame-options': 'SAMEORIGIN'
    },
    'href': 'https://feeds.finance.yahoo.com/rss/2.0/headline',
    'status': 400,
    'encoding': 'iso-8859-1',
    'version': '',
    'namespaces': {}
}
