ERROR_400_TEMPLATE_NAME = 'pages/page-400.html'
ERROR_403_TEMPLATE_NAME = 'pages/page-403.html'
ERROR_404_TEMPLATE_NAME = 'pages/page-404.html'
ERROR_500_TEMPLATE_NAME = 'pages/page-500.html'
ERROR_PAGE_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <title>%(title)s</title>
</head>
<body>
  <h1>%(title)s</h1><p>%(details)s</p>
</body>
</html>
"""
