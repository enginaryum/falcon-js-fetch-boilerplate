function api(endpoint, method = 'GET', body) {
  const baseUrl = 'http://127.0.0.1:8765/api'
  const url = baseUrl + endpoint
  const params = {
    headers: {
      'content-type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 'true'
    },
    method: method,
    body: JSON.stringify(body)
  }
  const request = new Request(url, params)
  fetch(request)
    .then(response => response.json())
    .then(data => {
        // Use json response
        console.log(data)
      }
    )
    .catch(error => {
      // Handle error
      console.log(error)
    })

}