# pw_images

### Scripts no terminal
```bash
mkdir project_pictures
cd project_pictures
python -m virtualenv venv
venv\Scripts\activate
pip install django
django-admin startproject config .
py manage.py startapp pictures
pip install django-cloudinary-storage
pip install Pillow  (para usar ImageField)
```

usamos package [django-cloudinary-storage](https://github.com/klis87/django-cloudinary-storage) que permite usar ImageField que guardam a imagem em Cloudinary

### Conta em [cloudinary.com](https://cloudinary.com/)
* criar conta em cloudinary 
* product: programmable media
* ir a dashboard onde se visualizam as configurações

### settings.py 

* em INSTALLED_APPS, adicionar 
```Python
INSTALLED_APPS += [
   'cloudinary_storage',
   'cloudinary',
   '<nome da aplicação criada>'
]
```
* incluir, no final do ficheiro, as credenciais da conta no cloudinary:
```python
CLOUDINARY_STORAGE = {
  'CLOUD_NAME': "your_Cloud_name",
  'API_KEY': "your_api_key",
  'API_SECRET': "your_api_secret",
}
```
   * na conta do cloudinary.com, no Dashboard, ir buscar os dados cloud_name, api_key, api_secret
   
* especificar nome da pasta a criar no cloudinary para guardar ficheiros da aplicação
```
MEDIA_URL = '/<nome da aplicaçao>/'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
### models.py

criar classe para as imagens usando ImageField e especificando nome da pasta (dentro da pasta especificada em MEDIA_URL) onde queremos guardar as imagens
```Python
from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures/', blank=True)
```

### admin.py
registar no admin o modelo Picture para podermos manipular na app admin

### terminal
```bash
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
```

### aplicação admin

* abrir aplicação admin, em 127.0.0.1/admin
* carregar fotos
* ver que no cloudinary ficaram carregadas. 
* se, no model,  mudarmos o valor de upload_to, será criada uma nova pasta

### views.py

criamos view index()
```python
from .models import Picture

def index(request):
    pictures = Picture.objects.all()
    ctx = {'pictures': pictures}
    return render(request, 'templates/media/index.html', ctx)
```

### index.html
* criamos pasta templates/media/
* criamos ficheiro index.html, com ciclo para incluir todas as fotos e seus nomes
```html
<body>
    <h1>Pictures</h1>
    {% for picture in pictures %}
        <img src="{{ picture.image.url }}">
        <h4>{{ picture.name }}</h4>
    {% endfor %}
</body>
```


### urls.py
* no config/urls.py, associamos à rota '' os urls de media.urls
    path('', include('media.urls'))
* no media/urls.py, criamos rota do url para a view index
```python
from django.urls import path
from . import views

app_name = 'media'
urlpatterns = [
    path('', views.index, name='index')
]
```


### forms.py
criar formulário para nova imagem 

```python
from django import forms
from .models import Picture

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'
```

### views.py
criar view para fazer upload de imagem

```python
def upload(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))

    form = PictureForm()
    ctx = {'form': form}
    return render(request, 'media/upload.html', ctx)
```


### urls.py
* em media/urls.py, criar rota do url load/ para a view load()
```python
urlpatterns += [
    path('load/', views.load, name='load')
]
```

### index.html
colocar no final das fotos, um link para carregar imagens
```html
<a href="{% url 'media:upload' %}">Carregar imagem</a>
```
colocar, para cada imagem, hiperlink para apagar imagem
```html
(<a href="{% url 'media:delete' picture.pk %}">apagar</a>)
```


### urls.py
* em media/urls.py, criar rota do url delete/picture_pk para a view delete()
```python
urlpatterns += [
    path('delete/<int:picture_pk>', views.delete, name='delete'),
]
```

### views.py
criar view para apagar imagem

```python
def delete(request, picture_pk):
    picture = Picture.objects.get(pk=picture_pk)
    picture.delete()
    return redirect(reverse('media:index'))
```

