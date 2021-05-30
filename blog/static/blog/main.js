function copyToClipboard(Text) {
    const elem = document.createElement('bi bi-share');
    elem.value = text;
    document.body.appendChild(elem);
    elem.select();
    document.execCommand('copy');
    document.body.removeChild(elem);
 }