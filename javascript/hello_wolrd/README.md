Hello World from Javascript
===================


A "Hello World!" program for Javascript

----------


I - What is Javascript?
-------------

Javascript is a **programming language** created specifically **for the Web**. Unlike, general-purpose languages (C, C++, Python, Java..), Javascript runs only in a browser and **IT CANNOT RUN INDEPENDENTLY**. It means that it must always be included within an HTML file. That's why it is recommended to have some knowledge about HTML and CSS before dealing with Javascript.

In what follows, I assume you already have some background in HTML.


II - "Hello World!"
-------------

1 - First, create a new file and copy/paste the code below.

```
<!DOCTYPE html>
<html>
<body>

<p>Click the button to show the alert box.</p>

<button onclick="showAlertBox()">Click me!</button>

<script>
function showAlertBox() {
    alert("Hello World! I am an alert box.");
}
</script>

</body>
</html>
```

2 - Save your file using the **.html** extension. (e.g. "HelloWorld.html").

3 - Go to where you saved your file and open it using it your favorite browser.

4 - Click the button...


Congratulations! You've just written your first Javascript program.


III - Let's examine this program
-------------

This "Hello World!" program shows you how to use an **alert box** to display a message to the user.

The part of the code above resposible for that is `alert("Hello World! I am an alert box.");`. Other than that, it is a typical HTML file.

Most importantly, this example shows you how to include your Javascript code within your HTML file, using the **<script></script>** tag.

When you click on the button, the **onclick** attribute call the function **showAlertBox()**. You browser will look for the deifinition of the function inside the **<script></script>** tag. This function tells the browser to show an **alert box** that displays the message **Hello World! I am an alert box.**.