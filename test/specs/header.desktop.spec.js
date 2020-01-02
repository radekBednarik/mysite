const expect = require('chai').expect
const Header = require('../pages/header.page')

describe('Desktop version of the site', function () {

    this.beforeAll(function () {
        Header.open('http://127.0.0.1:4200')
        Header.maximize()
    })

    context('header has all elements', function () {

        it('page title is correct', function () {
            expect(Header.pageTitleElementHTML()).includes(Header.title)
        })

        it('H1 header title is correct', function () {
            expect(Header.getText(Header.titleH1)).equals(Header.titleH1Text)
        })

    })

})
