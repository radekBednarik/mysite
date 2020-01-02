const Page = require('./page').default

class Header extends Page {

    constructor() {
        super()
        this.titleH1Text = 'Radek Bednarik software tester'
    }

    get titleH1() {
        return $('//*[@id="header"]/h1')
    }
}
module.exports = new Header()