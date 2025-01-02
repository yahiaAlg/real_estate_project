I'll help create this comprehensive Django tutorial. Given the extensive content, let's break this down into manageable sections. Let's start with Part 1: Search and Filtering.

Part 1: Search and Filtering

First, let's set up a sample model to use throughout our examples:

```python
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```

1. Basic Search Implementation:

```python
# views.py
from django.shortcuts import render
from django.db.models import Q
from .models import Product

def search_products(request):
    query = request.GET.get('q', '')
    
    if query:
        # Basic filter
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    return render(request, 'products/search.html', {
        'products': products,
        'query': query
    })

# Advanced search with Q objects
def advanced_search(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    products = Product.objects.all()
    
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    
    if category:
        products = products.filter(category=category)
    
    if min_price:
        products = products.filter(price__gte=min_price)
    
    if max_price:
        products = products.filter(price__lte=max_price)
    
    return render(request, 'products/advanced_search.html', {
        'products': products,
        'query': query,
        'category': category,
        'min_price': min_price,
        'max_price': max_price
    })
```

Template for the search functionality:

```html
<!-- templates/products/search.html -->
<form method="get" action="{% url 'search_products' %}">
    <input type="text" name="q" value="{{ query }}">
    <button type="submit">Search</button>
</form>

<div class="results">
    {% if products %}
        {% for product in products %}
            <div class="product">
                <h3>{{ product.name }}</h3>
                <p>{{ product.description }}</p>
                <p>Price: ${{ product.price }}</p>
                <p>Category: {{ product.category }}</p>
            </div>
        {% endfor %}
    {% else %}
        <p>No products found.</p>
    {% endif %}
</div>

<!-- templates/products/advanced_search.html -->
<form method="get" action="{% url 'advanced_search' %}">
    <div>
        <label>Search:</label>
        <input type="text" name="q" value="{{ query }}">
    </div>
    <div>
        <label>Category:</label>
        <input type="text" name="category" value="{{ category }}">
    </div>
    <div>
        <label>Min Price:</label>
        <input type="number" name="min_price" value="{{ min_price }}">
    </div>
    <div>
        <label>Max Price:</label>
        <input type="number" name="max_price" value="{{ max_price }}">
    </div>
    <button type="submit">Search</button>
</form>
```

Here's an example of combining multiple Q objects with complex conditions:

```python
# Complex Q object combinations
def complex_search(request):
    query = request.GET.get('q', '')
    
    if query:
        # Complex search criteria
        products = Product.objects.filter(
            (Q(name__icontains=query) | Q(description__icontains=query)) &
            (Q(price__gte=10.00) | Q(category='featured')) &
            ~Q(category='discontinued')  # Exclude discontinued products
        )
    else:
        products = Product.objects.all()
    
    return render(request, 'products/search.html', {
        'products': products,
        'query': query
    })
```

Best practices and optimization tips for search functionality:

```python
# utils.py
from django.db.models import Q
from functools import reduce
import operator

def normalize_query(query_string):
    """
    Normalize the query string by splitting it into individual terms
    and removing unnecessary whitespace.
    """
    return [term.strip() for term in query_string.split() if term.strip()]

def build_query(search_fields, query_terms):
    """
    Build a complex query combining multiple fields and terms.
    """
    queries = []
    for term in query_terms:
        term_queries = []
        for field in search_fields:
            term_queries.append(Q(**{f"{field}__icontains": term}))
        queries.append(reduce(operator.or_, term_queries))
    return reduce(operator.and_, queries)

# views.py
def optimized_search(request):
    query = request.GET.get('q', '')
    search_fields = ['name', 'description', 'category']
    
    if query:
        query_terms = normalize_query(query)
        search_query = build_query(search_fields, query_terms)
        
        # Use select_related() for foreign keys if needed
        products = Product.objects.filter(search_query).distinct()
    else:
        products = Product.objects.none()
    
    return render(request, 'products/search.html', {
        'products': products,
        'query': query
    })
```
---


Let's continue with Part 2: Complex Queries and Part 3: Pagination.

Part 2: Complex Queries

```python
# views.py
from django.db.models import F, Count, Avg, Max, Min
from django.db.models.functions import ExtractYear

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

# Complex query examples
def complex_queries_example(request):
    # Chaining filters
    expensive_recent_products = Product.objects.filter(
        price__gte=100
    ).filter(
        created_at__year=2024
    ).exclude(
        category='clearance'
    )

    # Annotate with calculated fields
    products_with_stats = Product.objects.annotate(
        total_ordered=Count('orderitem'),
        revenue=F('price') * F('orderitem__quantity')
    )

    # Complex aggregation
    category_stats = Product.objects.values('category').annotate(
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
        product_count=Count('id')
    )

    # Using F expressions for comparisons
    discounted_products = Product.objects.filter(
        sale_price__lt=F('regular_price') * 0.5
    )

    # Subqueries
    from django.db.models import Subquery, OuterRef
    latest_orders = OrderItem.objects.filter(
        product=OuterRef('pk')
    ).order_by('-order_date')

    products_with_last_order = Product.objects.annotate(
        last_ordered=Subquery(
            latest_orders.values('order_date')[:1]
        )
    )

    return render(request, 'products/complex_queries.html', {
        'expensive_recent_products': expensive_recent_products,
        'products_with_stats': products_with_stats,
        'category_stats': category_stats,
        'discounted_products': discounted_products,
        'products_with_last_order': products_with_last_order,
    })

# Query optimization example
def optimized_complex_query(request):
    # Use select_related for foreign keys
    products_with_related = Product.objects.select_related(
        'category', 'manufacturer'
    ).prefetch_related(
        'orderitem_set'  # Use prefetch_related for reverse relationships
    ).filter(
        price__gte=50
    )

    return render(request, 'products/optimized_queries.html', {
        'products': products_with_related
    })
```

Part 3: Pagination

1. Function-Based View Pagination:

```python
# views.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginated_products(request):
    product_list = Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 10)  # Show 10 products per page
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    return render(request, 'products/product_list.html', {'products': products})
```

2. Class-Based View Pagination:

```python
# views.py
from django.views.generic import ListView

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

# AJAX Pagination View
from django.template.loader import render_to_string
from django.http import JsonResponse

def ajax_product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)
    page = request.GET.get('page', 1)
    
    try:
        products = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        products = paginator.page(1)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string(
            'products/product_list_partial.html',
            {'products': products}
        )
        return JsonResponse({
            'html': html,
            'has_next': products.has_next()
        })
    
    return render(request, 'products/product_list.html', {'products': products})
```

Templates for pagination:

```html
<!-- templates/products/product_list.html -->
{% extends 'base.html' %}

{% block content %}
<div id="product-list">
    {% include 'products/product_list_partial.html' %}
</div>

<div class="pagination">
    {% if products.has_previous %}
        <a href="?page=1">&laquo; first</a>
        <a href="?page={{ products.previous_page_number }}">previous</a>
    {% endif %}

    <span class="current">
        Page {{ products.number }} of {{ products.paginator.num_pages }}
    </span>

    {% if products.has_next %}
        <a href="?page={{ products.next_page_number }}">next</a>
        <a href="?page={{ products.paginator.num_pages }}">last &raquo;</a>
    {% endif %}
</div>

<!-- AJAX Pagination JavaScript -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    const productList = document.getElementById('product-list');
    const loadMoreBtn = document.getElementById('load-more');
    let currentPage = 1;

    loadMoreBtn.addEventListener('click', function() {
        currentPage++;
        fetch(`?page=${currentPage}`, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            productList.insertAdjacentHTML('beforeend', data.html);
            if (!data.has_next) {
                loadMoreBtn.style.display = 'none';
            }
        });
    });
});
</script>
{% endblock %}

<!-- templates/products/product_list_partial.html -->
{% for product in products %}
    <div class="product-item">
        <h3>{{ product.name }}</h3>
        <p>{{ product.description }}</p>
        <p>Price: ${{ product.price }}</p>
    </div>
{% endfor %}
```

Part 4: Email Functionality

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your@email.com'
EMAIL_HOST_PASSWORD = 'your-app-specific-password'

# views.py
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection, EmailMessage
from django.conf import settings

def send_simple_email(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    return HttpResponse('Email sent!')

def send_html_email(request):
    subject = 'Welcome to our site'
    html_content = render_to_string(
        'emails/welcome.html',
        {'user': request.user}
    )
    text_content = strip_tags(html_content)
    
    email = EmailMultiAlternatives(
        subject,
        text_content,
        'from@example.com',
        ['to@example.com']
    )
    email.attach_alternative(html_content, "text/html")
    email.attach_file('path/to/attachment.pdf')
    email.send()
    
    return HttpResponse('HTML email sent!')

# Mass emailing with batch processing
def send_mass_emails(email_list, subject, template_name, context):
    connection = get_connection()
    messages = []
    
    for email_address in email_list:
        html_content = render_to_string(template_name, context)
        text_content = strip_tags(html_content)
        
        message = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [email_address],
        )
        message.attach_alternative(html_content, "text/html")
        messages.append(message)
    
    # Send emails in batches of 100
    batch_size = 100
    for i in range(0, len(messages), batch_size):
        batch = messages[i:i + batch_size]
        connection.send_messages(batch)

# Celery task for background email processing
from celery import shared_task

@shared_task
def send_async_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )
```

Email template example:

```html
<!-- templates/emails/welcome.html -->
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 600px; margin: 0 auto; }
        .button { 
            background: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome, {{ user.username }}!</h1>
        <p>Thank you for joining our platform.</p>
        <p>
            <a href="{{ verification_url }}" class="button">
                Verify Your Email
            </a>
        </p>
    </div>
</body>
</html>
```

---

I'll break down the logic and concepts behind each major section.

Part 1: Search and Filtering Logic

1. Basic Search:
```python
products = Product.objects.filter(name__icontains=query)
```
- `filter()`: Acts like SQL's WHERE clause
- `icontains`: Case-insensitive containment test (like SQL's LIKE %query%)
- This searches for the query string anywhere in the product name

2. Advanced Search Logic:
```python
Q(name__icontains=query) | Q(description__icontains=query)
```
- `Q` objects allow complex queries with OR (|) and AND (&) operations
- This searches in both name AND description fields
- The `|` operator means "OR" - matches if either condition is true

3. Query Building:
```python
def build_query(search_fields, query_terms):
    queries = []
    for term in query_terms:
        term_queries = []
        for field in search_fields:
            term_queries.append(Q(**{f"{field}__icontains": term}))
        queries.append(reduce(operator.or_, term_queries))
    return reduce(operator.and_, queries)
```
Logic flow:
1. Split search terms (e.g., "blue shirt" → ["blue", "shirt"])
2. For each term, create a query across all fields
3. Combine field queries with OR (match any field)
4. Combine term queries with AND (match all terms)

Part 2: Complex Queries Logic

1. Chaining Filters:
```python
expensive_recent_products = Product.objects.filter(
    price__gte=100
).filter(
    created_at__year=2024
).exclude(
    category='clearance'
)
```
- Filters are applied sequentially
- Django optimizes this into a single SQL query
- Like SQL: WHERE price >= 100 AND YEAR(created_at) = 2024 AND category != 'clearance'

2. Annotations:
```python
products_with_stats = Product.objects.annotate(
    total_ordered=Count('orderitem'),
    revenue=F('price') * F('orderitem__quantity')
)
```
- `annotate`: Adds computed fields to each object
- `F` expressions refer to model fields
- Calculations happen in the database, not Python

Part 3: Pagination Logic

1. Basic Pagination:
```python
paginator = Paginator(product_list, 10)
try:
    products = paginator.page(page)
except PageNotAnInteger:
    products = paginator.page(1)
except EmptyPage:
    products = paginator.page(paginator.num_pages)
```
Flow:
1. Create Paginator with items and page size
2. Handle three cases:
   - Valid page number → show requested page
   - Invalid number → show first page
   - Page out of range → show last page

2. AJAX Pagination Logic:
```python
if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    html = render_to_string(
        'products/product_list_partial.html',
        {'products': products}
    )
    return JsonResponse({
        'html': html,
        'has_next': products.has_next()
    })
```
Flow:
1. Check if request is AJAX
2. If AJAX: return HTML fragment + pagination state
3. If regular request: return full page

Part 4: Email Functionality Logic

1. Basic Email:
```python
send_mail(
    subject,
    message,
    from_email,
    recipient_list,
    fail_silently=False,
)
```
- Simple wrapper around Python's email functionality
- Handles connection management automatically
- Uses configured email backend

2. HTML Email Logic:
```python
html_content = render_to_string('emails/welcome.html', context)
text_content = strip_tags(html_content)
email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
email.attach_alternative(html_content, "text/html")
```
Flow:
1. Render HTML template
2. Create plain text fallback
3. Create email with plain text
4. Attach HTML version as alternative
5. Email clients choose best format to display

3. Mass Email Logic:
```python
def send_mass_emails(email_list, subject, template_name, context):
    connection = get_connection()
    messages = []
    # Create messages
    for i in range(0, len(messages), batch_size):
        batch = messages[i:i + batch_size]
        connection.send_messages(batch)
```
Flow:
1. Reuse single connection for multiple emails
2. Create all email messages first
3. Send in batches to avoid overwhelming server
4. Single connection reduces overhead

4. Background Email Processing:
```python
@shared_task
def send_async_email(subject, message, recipient_list):
    send_mail(...)
```
Logic:
- Decorator marks function as Celery task
- Executes in separate worker process
- Doesn't block main application
- Can be retried on failure

Key Optimizations:

1. Database:
- Use `select_related()` for foreign keys
- Use `prefetch_related()` for reverse relationships
- Create indexes on frequently searched fields

2. Queries:
- Filter as early as possible
- Use database-level operations instead of Python
- Combine queries when possible instead of multiple database hits

3. Pagination:
- Limit query results to current page
- Use AJAX to load more content dynamically
- Cache paginated results when possible

4. Emails:
- Use connection pooling for mass emails
- Process emails in background
- Provide both HTML and plain text versions
- Use templates for consistent formatting
