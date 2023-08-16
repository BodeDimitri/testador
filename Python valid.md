### Python valid

#### Factory Method:

Cria objetos tendo em vista que as subclasses decidiram qual classe instanciar 

```python
class Documento:

    @staticmethod
    def cria_documentos(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos esta incorreta")
```

Nesse trecho de código esta sendo definido se a classe a ser instanciada sera a DocCpf ou DocCnpj, baseando na quantidade de números que foram passados. 

> Classes>subclasses>objetos.

---

#### Regex:

- [] Define range e número de caracteres. 

> [0-9; [a-z]; [abc]

- \* Marca nenhuma, uma ou mais ocorrência

> sol*

- {} Quantidade de repetições de uma ocorrência

> [abc]{5}

- \d Qualquer número de 0 até 9

> \d

- \w Qualquer número, qualquer letra e incluindo underline

> \w

- | Um ou outro

> @|\

- () Captura e agrupa - Relação com o find

> (\w{4})

**re.findall** - Vai retornar todas as repostas que se encaixam no padrão.

**re.search** - Vai retornar apenas a primeira correspondência.

> {objeto}.group(campo) E possível escolher o campo que o será exibido

```python
resposta = re.search(padrao, self.numero)
numero_formatado = "+{} ({}) {}-{}".format (
    resposta.group(1),
    resposta.group(2),
    resposta.group(3),
    resposta.group(4)
)
```

- ? Torna uma sequencia de caracteres ou números opcional

---

#### Datetime

Datetime e timedelta, todos estão relacionados ao horário.

- datetime.today() - retorna o dia e o horário. 

- datetime.weekday() - Retorna o dia da semana.

- datetime.month - Retorna o mês do ano.

---

#### Strftime

.strftime({Aqui você especifica os %})

- %A - Dias da semana escritos.

- %d - Dia do mês em número.

- %m - Mês em formato de número.

- %y - Ano em número, representado por dois dígitos.

- %Y - Ano em número, representado por quatro dígitos.

- %H - Hora no formato decimal.

- %M - Minuto em forma decimal.

- %S - Segundo em forma decimal.

**timedelta({data}**) - E usado para fazer calcular diferença entre datas e manipular datas.

```python
datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) 
```

---

#### Requests

Requests e uma biblioteca do Python que permite o recebimento e envio de informações pelos métodos **get  e  post**.

- requests.get({link})

```python
r = requests.get("http://date.jsontest.com/")

Output=
{
   "date": "06-22-2023",
   "milliseconds_since_epoch": 1687437103411,
   "time": "12:31:43 PM"
}
```

A diferença entre JSON e text e que:

- text retorna uma string.

- JSON vem como dicionário/dict.

```python
print(type(a.text))
print(type(a.json()))
```

> {
>   "cep": "01001-000",
>   "logradouro": "Praça da Sé",
>   "complemento": "lado ímpar",
>   "bairro": "Sé",
>   "localidade": "São Paulo",
>   "uf": "SP",
>   "ibge": "3550308",
>   "gia": "1004",
>   "ddd": "11",
>   "siafi": "7107"
> } 
> 
> > Retorno do text

> {'cep': '01001-000', 'logradouro': 'Praça da Sé', 'complemento': 'lado ímpar', 'bairro': 'Sé', 'localidade': 'São Paulo', 'uf': 'SP', 'ibge': '3550308', 'gia': '1004', 'ddd': '11', 'siafi': '7107'}      
> 
> > Retorno do JSON

Se você estiver usando um JSON você pode pesquisar pelo *[' ']* 

```python
print(a.json()['cep'])
print(a.json()['bairro'])
```

> 'Sé', 'São Paulo'

---

Dentro da `request line` é importante destacar o método 
utilizado. Este método também é conhecido como verbo HTTP, que indica 
qual ação deve ser executada no servidor. Os verbos mais utilizados são 
os seguintes:

`GET`: Solicita informações de um recurso; `POST`: Cria um recurso; `PUT`: Atualiza um recurso; `DELETE`: Remove um recurso. [Referência](https://blog.alura.com.br/diferencas-entre-get-e-post/)
