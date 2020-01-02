const expect = require('chai').expect
const NavBar = require('../pages/navbar.page')

describe('Desktop version of the site', function () {

    this.beforeAll(function () {
        NavBar.open('http://127.0.0.1:4200')
        NavBar.maximize()
    })

    context('navbar has all elements', function () {

        it('icon is displayed', function () {
            expect(NavBar.iconIsDisplayed()).to.be.true
        })

        it('navbarToggle is in HTML', function () {
            expect(NavBar.navbarTogglerIsLoadedInHTML()).to.be.true
        })

        it('About link is visible and has text', function () {
            expect(NavBar.getText(NavBar.linkAbout)).equals(NavBar.about)
        })

        it('Skills link is visible and has text', function () {
            expect(NavBar.getText(NavBar.linkSkills)).equals(NavBar.skills)
        })

        it('Projects link is visible and has text', function () {
            expect(NavBar.getText(NavBar.linkProjects)).equals(NavBar.projects)
        })

        it('Code link is visible and has text', function () {
            expect(NavBar.getText(NavBar.linkCode)).equals(NavBar.code)
        })
        

    })

})
