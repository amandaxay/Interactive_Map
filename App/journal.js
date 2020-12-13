var today = new Date();
var expiry = new Date(today.getTime() + 30 * 24 * 3600 * 1000); // plus 30 days

function setCookie(name, value)
{
  document.cookie=name + "=" + escape(value) + "; path=/; expires=" + expiry.toUTCString();
}

function storeValues(form)
{
  setCookie("field1", form.getElementById("field1").value);
  setCookie("field2", form.getElementById("field2").value);
  return true;
}

function getCookie(name)
{
  var re = new RegExp(name + "=([^;]+)");
  var value = re.exec(document.cookie);
  return (value != null) ? unescape(value[1]) : null;
}


const expired = new Date(today.getTime() - 24 * 3600 * 1000); // less 24 hours

function deleteCookie(name)
{
  document.cookie=name + "=null; path=/; expires=" + expired.toUTCString();
}

function clearCookies()
{
    deleteCookie("field1");
    deleteCookie("field2");
    alert('Your cookies have been deleted!');
}

function display()
{
  document.write(getCookie("field1"));
  document.write(getCookie("field2"));
}
