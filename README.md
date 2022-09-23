# api-cotizacion-brou-requests
-------------------------------------------

## Run with: 

`cd /app`

`uvicorn app:app --reload`

-------------------------------------------
### Request:
`curl -X 'GET'   'http://127.0.0.1:8000/cotizacion'   -H 'accept: application/json'`


### Response:
```
{
  "status": "Success",
  "code": "200",
  "data": [
    {
      "Dólar": {
        "Compra": "39,45000",
        "Venta": "41,85000"
      },
      "Dólar eBROU": {
        "Compra": "39,95000",
        "Venta": "41,35000"
      },
      "Euro": {
        "Compra": "37,88000",
        "Venta": "42,36000"
      },
      "Peso Argentino": {
        "Compra": "0,05000",
        "Venta": "0,35000"
      },
      "Real": {
        "Compra": "7,10000",
        "Venta": "9,10000"
      },
      "Libra Esterlina": {
        "Compra": "43,37000",
        "Venta": "48,94000"
      },
      "Franco Suizo": {
        "Compra": "39,62000",
        "Venta": "43,58000"
      },
      "Guaraní": {
        "Compra": "0,00551",
        "Venta": "0,00609"
      },
      "Unidad Indexada": {
        "Compra": "-",
        "Venta": "5,53720"
      },
      "Onza Troy De Oro": {
        "Compra": "65.325,25500",
        "Venta": "70.504,27650"
      }
    }
  ]
}
```
