# **Django Pagination: A Complete Beginner's Guide**

## **What is Pagination?**
Pagination divides content into discrete pages. In web applications, this is useful when displaying a large list of items like blog posts, products, or user data.

---

## **Setup: Getting Started with Django**

### Step 1: Install Django
Make sure you have Django installed. You can install it via pip:
```bash
pip install django
```

### Step 2: Create a Django Project and App
```bash
django-admin startproject pagination_project
cd pagination_project
python manage.py startapp pagination_app
```

### Step 3: Configure the App
Add `pagination_app` to your project's `INSTALLED_APPS` in `settings.py`.

---

## **Adding Models**
In `pagination_app/models.py`, create a simple model for demonstration:
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

Run migrations to create the database table:
```bash
python manage.py makemigrations
python manage.py migrate
```

### **Populate the Database**
Add some dummy data in the database. You can use Django's shell:
```bash
python manage.py shell
```
```python
from pagination_app.models import Item
for i in range(1, 101):
    Item.objects.create(name=f'Item {i}')
```

---

## **Using Django’s Built-in Paginator**
Django provides a `Paginator` class in `django.core.paginator`.

### **Views**
In `pagination_app/views.py`, use the Paginator:
```python
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Item

def item_list(request):
    items = Item.objects.all()  # Fetch all items
    paginator = Paginator(items, 10)  # Show 10 items per page

    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page object

    return render(request, 'pagination_app/item_list.html', {'page_obj': page_obj})
```

---

## **Creating the Template**
Create a template file `pagination_app/templates/pagination_app/item_list.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Item List</title>
</head>
<body>
    <h1>Items</h1>
    <ul>
        {% for item in page_obj %}
            <li>{{ item.name }}</li>
        {% endfor %}
    </ul>

    <!-- Pagination Controls -->
    <div>
        <span>
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
        </span>
    </div>
    <div>
        {% if page_obj.has_previous %}
            <a href="?page=1">First</a>
            <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
        {% endif %}

        {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
                <strong>{{ num }}</strong>
            {% else %}
                <a href="?page={{ num }}">{{ num }}</a>
            {% endif %}
        {% endfor %}

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">Next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">Last</a>
        {% endif %}
    </div>
</body>
</html>
```

---

## **Adding URL Patterns**
In `pagination_app/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
]
```

Include it in the project’s main `urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagination_app.urls')),
]
```

---

## **Run the Server**
Run the development server:
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## **Key Features Explained**

1. **`Paginator` Class**: Handles the division of data into pages.
2. **`get_page()` Method**: Ensures invalid page numbers don't break your app.
3. **Template Controls**:
   - **`page_obj.has_previous`**: Checks if there's a previous page.
   - **`page_obj.has_next`**: Checks if there's a next page.
   - **`page_obj.paginator.page_range`**: Provides a range of all page numbers.

---

## **Improving the UI**
Consider using a CSS framework like Bootstrap for better styling:
```html
<nav>
    <ul class="pagination">
        {% if page_obj.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page=1">First</a>
            </li>
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">Previous</a>
            </li>
        {% endif %}

        {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
                <li class="page-item active">
                    <span class="page-link">{{ num }}</span>
                </li>
            {% else %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ num }}">{{ num }}</a>
                </li>
            {% endif %}
        {% endfor %}

        {% if page_obj.has_next %}
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.next_page_number }}">Next</a>
            </li>
            <li class="page-item">
                <a class="page-link" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
            </li>
        {% endif %}
    </ul>
</nav>
```

---

Django divides data into pages using the `Paginator` class, which breaks a dataset (like a queryset) into chunks of manageable sizes, each represented as a page. Here's a detailed explanation of how it works:

---

### **1. Fetching the Data**
The data to be paginated is typically a Django queryset, such as:
```python
items = Item.objects.all()
```

This queryset contains all the records of the `Item` model from the database.

---

### **2. Creating the Paginator**
The `Paginator` class takes two main arguments:
- **The data to paginate**: A queryset or a list.
- **The number of items per page**: An integer specifying how many items should appear on each page.

```python
from django.core.paginator import Paginator

paginator = Paginator(items, 10)  # Divides `items` into pages with 10 items each
```

The `Paginator` divides the queryset into chunks based on the number specified. For example:
- If `items` has 50 records and the page size is 10, `Paginator` creates 5 pages.

---

### **3. Accessing Pages**
To access a specific page, use the `get_page()` or `page()` method:
```python
page_number = 2  # Example: Get the second page
page_obj = paginator.get_page(page_number)
```

#### What `get_page()` Returns:
- A `Page` object representing the requested page.
- Handles invalid page numbers gracefully:
  - If the page number is out of range, it defaults to the last or first page.

---

### **4. The `Page` Object**
The `Page` object contains the data for the specific page and provides helpful attributes:
- **Data on the Page**: Iterable containing the items for the current page:
  ```python
  for item in page_obj:
      print(item.name)
  ```
- **Page Information**:
  - `page_obj.number`: The current page number.
  - `page_obj.paginator.num_pages`: Total number of pages.
  - `page_obj.has_previous`: Boolean indicating if a previous page exists.
  - `page_obj.has_next`: Boolean indicating if a next page exists.

---

### **5. Example of Data Division**
Suppose we have 25 items in the database and set 10 items per page:
```python
paginator = Paginator(items, 10)
```

The data will be divided as follows:
- **Page 1**: Items 1–10
- **Page 2**: Items 11–20
- **Page 3**: Items 21–25

Requesting `paginator.get_page(1)` will return:
```python
<Item: Item 1>, <Item: Item 2>, ..., <Item: Item 10>
```

---

### **6. Customizing the Division**
You can customize the number of items per page by adjusting the second argument to the `Paginator` class:
```python
paginator = Paginator(items, 5)  # 5 items per page
```
This changes the data division as follows:
- **Page 1**: Items 1–5
- **Page 2**: Items 6–10
- **Page 3**: Items 11–15
- **Page 4**: Items 16–20
- **Page 5**: Items 21–25

---

### **7. Handling Page Numbers in Views**
The page number is usually passed as a query parameter in the URL:
```python
http://example.com/items?page=2
```

In the view, you retrieve the page number:
```python
page_number = request.GET.get('page')  # Get the 'page' query parameter
page_obj = paginator.get_page(page_number)
```

The `get_page()` method handles invalid or missing page numbers by default.

---

### **8. Displaying the Pages**
In your template, you iterate over the items in the `Page` object and use its attributes to create navigation controls:
```html
<ul>
    {% for item in page_obj %}
        <li>{{ item.name }}</li>
    {% endfor %}
</ul>
```

Pagination controls:
```html
{% if page_obj.has_previous %}
    <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
{% endif %}

{% if page_obj.has_next %}
    <a href="?page={{ page_obj.next_page_number }}">Next</a>
{% endif %}
```

---