# COWIN-slot-availability
A python script to check availability of vaccine slots using district id.

The government has released the [Co-WIN API](https://apisetu.gov.in/public/marketplace/api/cowin/cowin-protected-v2#/Vaccination%20Appointment%20APIs/calendarByDistrict) to the public. It helps people do almost everything that can be done on the [Co-WIN website](https://www.cowin.gov.in/home). Due to the shortage of vaccines, it has been very difficult to find slots for people in the 18-45 category.

I wrote a simple Lambda function in python that uses [AWS EventBridge](https://docs.aws.amazon.com/eventbridge/index.html) and [AWS SNS](https://ap-south-1.console.aws.amazon.com/sns/v3/home?region=ap-south-1#/homepage) to automatically check for slots every minute and send me an email with the details of the vaccination centre whenever they open.
