import re
def fun(s):
    regex = r'^[a-zA-Z\d\-\_]+@[a-zA-Z\d]+\.[a-zA-Z]{0,3}$'
    e_filter = lambda email,regex: email if(len(re.findall(regex,email))>0) else ''
    return(e_filter(s,regex))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
