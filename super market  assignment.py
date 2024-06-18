import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def super_market():
    print("*** Welcome to Beasant Super Market ***")
def market():
    grocery_items = ["tomato", "potato", "onion", "coconut", "beetroot"]
    cosmetic_items = ["shampoo", "soap", "perfume", "lotion", "lipstick"]
    baby_items = ["diapers", "baby oil", "baby shampoo", "baby lotion", "baby powder"]
    household_items = ["detergent", "cleaning brush", "dish soap", "trash bags", "broom"]
    gst_rate = 0.18  
    grocery_prices = {"tomato": 40, "potato": 30, "onion": 80, "coconut": 60, "beetroot": 50}
    cosmetic_prices = {"shampoo": 150, "soap": 50, "perfume": 350, "lotion": 200, "lipstick": 120}
    baby_prices = {"diapers": 300, "baby oil": 200, "baby shampoo": 150, "baby lotion": 180, "baby powder": 120}
    household_prices = {"detergent": 250, "cleaning brush": 80, "dish soap": 120, "trash bags": 150, "broom": 180}
    try:
        your_order = input("Enter your order: ").lower()
        if your_order in grocery_items:
            print(f"Yes! {your_order} is available in grocery section.")
            how_many = int(input(f"How many kgs of {your_order} do you want: "))
            total_before_gst = grocery_prices[your_order] * how_many
            gst_amount = total_before_gst * gst_rate
            total_with_gst = total_before_gst + gst_amount
            print(f"Your total bill before GST is: {total_before_gst}")
            print(f"GST (18%) on your order is: {gst_amount}")
            print(f"Your total bill including GST is: {total_with_gst}")
            with open("bill.txt", "a") as f:
                f.write(f"Order: {your_order}\n")
                f.write(f"Total bill before GST: {total_before_gst}\n")
                f.write(f"GST (18%): {gst_amount}\n")
                f.write(f"Total bill including GST: {total_with_gst}\n")
                f.write("--------------------\n")
                print("Bill generated successfully")
        elif your_order in cosmetic_items:
            print(f"Yes! {your_order} is available in cosmetic section.")
            how_many = int(input(f"How many units of {your_order} do you want: "))
            total_before_gst = cosmetic_prices[your_order] * how_many
            gst_amount = total_before_gst * gst_rate
            total_with_gst = total_before_gst + gst_amount
            print(f"Your total bill before GST is: {total_before_gst}")
            print(f"GST (18%) on your order is: {gst_amount}")
            print(f"Your total bill including GST is: {total_with_gst}")
            with open("bill.txt", "a") as f:
                f.write(f"Order: {your_order}\n")
                f.write(f"Total bill before GST: {total_before_gst}\n")
                f.write(f"GST (18%): {gst_amount}\n")
                f.write(f"Total bill including GST: {total_with_gst}\n")
                f.write("--------------------\n")
                print("Bill generated successfully")
        elif your_order in baby_items:
            print(f"Yes! {your_order} is available in baby products section.")
            how_many = int(input(f"How many units of {your_order} do you want: "))
            total_before_gst = baby_prices[your_order] * how_many
            gst_amount = total_before_gst * gst_rate
            total_with_gst = total_before_gst + gst_amount
            print(f"Your total bill before GST is: {total_before_gst}")
            print(f"GST (18%) on your order is: {gst_amount}")
            print(f"Your total bill including GST is: {total_with_gst}")
            with open("bill.txt", "a") as f:
                f.write(f"Order: {your_order}\n")
                f.write(f"Total bill before GST: {total_before_gst}\n")
                f.write(f"GST (18%): {gst_amount}\n")
                f.write(f"Total bill including GST: {total_with_gst}\n")
                f.write("--------------------\n")
                print("Bill generated successfully")
        elif your_order in household_items:
            print(f"Yes! {your_order} is available in household products section.")
            how_many = int(input(f"How many units of {your_order} do you want: "))
            total_before_gst = household_prices[your_order] * how_many
            gst_amount = total_before_gst * gst_rate
            total_with_gst = total_before_gst + gst_amount
            print(f"Your total bill before GST is: {total_before_gst}")
            print(f"GST (18%) on your order is: {gst_amount}")
            print(f"Your total bill including GST is: {total_with_gst}")
            with open("bill.txt", "a") as f:
                f.write(f"Order: {your_order}\n")
                f.write(f"Total bill before GST: {total_before_gst}\n")
                f.write(f"GST (18%): {gst_amount}\n")
                f.write(f"Total bill including GST: {total_with_gst}\n")
                f.write("--------------------\n")
                print("Bill generated successfully")
        else:
            print(f"Sorry, {your_order} is not available.")
        send_bill_email(your_order, total_before_gst, gst_amount, total_with_gst)
        var = input("If you want to continue shopping, press 'yes': ").lower()
        if var == "yes":
            market()
        else:
            print("*** Thanks for visiting our Beasant Super Market ***")
    except ValueError:
        print("Please type a number only.")
    except Exception as e:
        print(f"An error occurred: {e}")
def send_bill_email(item, total_before_gst, gst_amount, total_with_gst):
    sender_email = "dineshdinesh112004@gmail.com"  
    sender_password = "svtq oaiw tofj hvpf" 
    receiver_email = "rathinamdinesh92@gmail.com"  
    subject = "Your Supermarket Bill"
    body = f"Thank you for shopping with us!\n\n" \
           f"Item: {item}\n" \
           f"Total bill before GST: {total_before_gst}\n" \
           f"GST (18%): {gst_amount}\n" \
           f"Total bill including GST: {total_with_gst}\n\n" \
           f"Have a great day!"
    msg = MIMEMultipart()
    msg['From'] = "dineshdinesh112004@gmail.com"
    msg['To'] = "rathinamdinesh92@gmail.com"
    msg['Subject'] = "your supermarket bill"
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login("dineshdinesh112004@gmail.com","svtq oaiw tofj hvpf")
        text = msg.as_string()
        server.sendmail("dineshdinesh112004@gmail.com", "rathinamdinesh92@gmail.com", text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
super_market()
market()
