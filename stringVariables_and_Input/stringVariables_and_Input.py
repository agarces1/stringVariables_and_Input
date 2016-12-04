#The input function allows you to specify a message to display and returns the value typed in by the user; use names that make sense.
#Collects name from user
name = input("What is your name?");
print(name);
#update the value
name = 'Mary'
print("Value updated to " + name)
#Examples of good variable names
FirstName = input("What is your first name?");
lastName = input("What is your last name?");
print("Hello " + FirstName + " " + lastName);
#Basic text manipulation
message = 'Hello World'
print(message.lower());
print(message.upper());
print(message.swapcase());
print(message.replace('Hello', 'Hi'));