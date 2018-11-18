/*
interface Element {
    name: String,
    description: String
    editLink: String
}
 */

class MenuGrid {
    constructor(element/*: JQHTMLElement*/, items/*: [Element]*/, deleteFunction/*: (String) => ()*/) {
        this.element = element
        this.items = items
        this.deleteFunction = deleteFunction
    }

    createElement(item/*: Element*/) {
        let e = $(`
            <div id="${item.name}" class="card">
                <div class="card-body">
                    <h5 class="card-title">${item.name}</h5>
                    <p class="card-text">${item.description}</p>
                    <hr/>
                    <a class="card-link" href="${item.editLink}">Edit</a>
                    <a class="card-link delete-link" href="#">Delete</a>
                </div>
            </div>
        `)

        e.find('.delete-link').on('click', () => this.deleteFunction(item.name))

        return e
    }

    render() {
        for (let e in this.items) {
            this.createElement(this.items[e]).appendTo(this.element)
        }
    }

    addItems(items/*: Element|[Element]*/) {
        if (!Array.isArray(items)) {
            items = [items]
        }

        for (let i in items) {
            $(this.createElement(items[i])).appendTo(this.element)
        }
    }

    removeItems(items/*: Element|[Element]*/) {
        if (!Array.isArray(items)) {
            items = [items]
        }

        for (let i in items) {
            $(this.element).children('#' + items[i].name).remove();
        }
    }
}