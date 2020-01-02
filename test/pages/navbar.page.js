const Page = require('./page').default

class NavBar extends Page {

    constructor() {
        super()
        this.about = 'About'
        this.skills = 'Skills'
        this.projects = 'Projects'
        this.code = 'Code'
    }

    get icon() {
        return $('//i[@class="fas fa-terminal"]')
    }

    get navbarToggler() {
        return $('//*[@id="navbar"]/nav/button')
    }

    get linkAbout() {
        return $('//*[@id="navbar-item-2"]')
    }

    get linkSkills() {
        return $('//*[@id="navbar-item-3"]')
    }

    get linkProjects() {
        return $('//*[@id="navbar-item-4"]')
    }

    get linkCode() {
        return $('//*[@id="navbar-item-5"]')
    }

    iconIsDisplayed() {
        this.icon.waitForDisplayed(10000)
        return this.icon.isDisplayed()
    }

    navbarTogglerIsLoadedInHTML() {
        this.navbarToggler.waitForExist(10000)
        return this.navbarToggler.isExisting()
    }

}
module.exports = new NavBar()