const toggleCryption = () => {
    const decryptTextArea = document.getElementById('decryptTextArea')
    const encryptTextArea = document.getElementById('encryptTextArea')

    if (decryptTextArea.disabled) {
        decryptTextArea.disabled = false
        document.getElementById("cryptText").innerHTML = "encrypt"
        encryptTextArea.placeholder = "Waiting..."
        decryptTextArea.placeholder = "Insert text..."

    } else {
        decryptTextArea.disabled = true
    }

    if (encryptTextArea.disabled) {
        encryptTextArea.disabled = false
        document.getElementById("cryptText").innerHTML = "decrypt"
        decryptTextArea.placeholder = "Waiting..."
        encryptTextArea.placeholder = "Insert text..."
    } else {
        encryptTextArea.disabled = true
    }
}