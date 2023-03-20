const url = 'http://10.10.16.12/api/portal/v1/login'
const headers = {
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'X-Requested-With': 'XMLHttpRequest'
}
const body = 'domain=telecom&username=ffffff&password=ffffff'

$httpClient.post(url, {
  headers: headers,
  body: body
}, (error, response, data) => {
  if (error) {
    $notification.post('登录失败', error, '')
    $done()
  } else {
    const result = JSON.parse(data)
    if (result.success) {
      $notification.post('登录成功', '欢迎使用', result.message)
      $done()
    } else {
      $notification.post('登录失败', result.message, '')
      $done()
    }
  }
})

