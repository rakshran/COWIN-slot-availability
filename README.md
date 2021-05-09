# COWIN-slot-availability
A python script to check availability of vaccine slots in district

The government has released the [Co-WIN API](https://apisetu.gov.in/public/marketplace/api/cowin/cowin-protected-v2#/Vaccination%20Appointment%20APIs/calendarByDistrict) to the public. It helps people do almost everything that can be done on the Co-WIN website. Due to the shortage of vaccines, it has been very difficult to find slots for people in the 18-45 category.

I wrote a simple Lambda function in python that works with [AWS EventBridge](https://docs.aws.amazon.com/eventbridge/index.html) and [AWS SNS](https://ap-south-1.console.aws.amazon.com/sns/v3/home?region=ap-south-1#/homepage).

It automatically checks for slots every minute and sends an email to me with the details of the vaccination centre whenever they open.
