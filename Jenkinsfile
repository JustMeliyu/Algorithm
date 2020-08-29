$ aws elbv2 modify-listener --listener-arn arn:aws:elasticloadbalancing:us-east-1:1234567890:listener/app/my-alb/123456789 --default-actions
 '[{"Type": "redirect", "RedirectConfig": {"Protocol": "HTTPS", "Port": "443", "Host": "#{host}", "Query": "#{query}", "Path": "/#{path}", "StatusCode": "HTTP_301"}}]'

def defaultActions = '[{\\"Type\\": \\"redirect\\", \\"RedirectConfig\\": {\\"Protocol\\": \\"HTTPS\\", \\"Port\\": \\"443\\", \\"Host\\": \\"#{host}\\", \\"Query\\": \\"#{query}\\", \\"Path\\": \\"/#{path}\\", \\"StatusCode\\": \\"HTTP_301\\"}}]'
sh """
    aws elbv2 modify-listener --listener-arn arn:aws:elasticloadbalancing:us-east-1:1234567890:listener/app/my-alb/123456789 --default-actions \\'${defaultActions}\\'
"""