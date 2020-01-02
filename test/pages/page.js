module.exports.default = class Page {
    constructor() {
        this.title = 'Radek Bednarik'
    }

    get pageTitle() {
        return $('/html/head/title')
    }

    open(url) {
        browser.url(url)
    }

    maximize() {
        browser.maximizeWindow()
    }

    close() {
        browser.closeWindow()
    }

    reloadSession() {
        browser.reloadSession()
    }

    getText(element) {
        return element.getText()
    }

    pageTitleElementHTML() {
        this.pageTitle.waitForExist(10000)
        return this.pageTitle.getHTML()
    }
}