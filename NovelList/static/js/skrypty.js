function cpt(el,el2)
{
    // alert(el);
    // alert(document.getElementById(el));
    // alert(document.getElementById(el).innerHTML);
    // alert(el2);
    if (location.protocol !== 'https:') {
        var textArea = document.createElement("textarea");
        textArea.style.position = 'fixed';
        textArea.style.top = 0;
        textArea.style.left = 0;
        textArea.style.width = '2em';
        textArea.style.height = '2em';
        textArea.style.padding = 0;
        textArea.style.border = 'none';
        textArea.style.outline = 'none';
        textArea.style.boxShadow = 'none';
        textArea.style.background = 'transparent';
        textArea.value = document.getElementById(el).innerHTML.length == 0 ? "No link" : document.getElementById(el).innerHTML;
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        textArea.setSelectionRange(0, 99999);
        try 
        {
            var successful = document.execCommand('copy');
            // alert('Skopiowano');
            var tooltip = document.getElementById(el2);
            tooltip.innerHTML = "Skopiowano: " + textArea.value;
            alert(tooltip.innerHTML);
        } 
        catch (err) 
        {
            var tooltip = el2;
            tooltip.innerHTML = "Unable: " + textArea.value;
        };
        document.body.removeChild(textArea);
    }
    else
    {
        var copyText = document.getElementById(el).innerHTML;
        navigator.clipboard.writeText(copyText).then(() => 
        {
        var tooltip = el2;
        tooltip.innerHTML = "Skopiowano: " + copyText;
        });
    }
}
function test()
{
    alert('wtf');
}
function vh(v) {
    var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
    return (v * h) / 100;
  }
  
  function vw(v) {
    var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    return (v * w) / 100;
  }
function outFunc(el) {
    // alert(el);
    var tooltip = document.getElementById(el);
    tooltip.innerHTML = "Kopiuj do schowka";
  }