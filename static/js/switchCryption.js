const toggleCryption = () => {
    const decryptArea = document.getElementById('decryptTextArea')
    const encryptTextArea = document.getElementById('encryptTextArea')

    if (decryptArea.disabled) {
        decryptArea.disabled = false
    } else {
        decryptArea.disabled = true
    }

    if (encryptTextArea.disabled) {
        encryptTextArea.disabled = false
    } else {
        encryptTextArea.disabled = true
    }
}