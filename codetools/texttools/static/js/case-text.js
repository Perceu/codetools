const cE = React.createElement;

class LikeButton extends React.Component {
    constructor(props) {
        super(props);

        this.handleChange = this.handleChange.bind(this);

        this.state = {
            value: "Digite usando espacos que crio o case pra voce"
        };
    }

    handleChange(e) {
        this.setState({ value: e.target.value });
    }

    getUpperCase() {
        return this.state.value.toUpperCase()
    }

    getLowerCase() {
        return this.state.value.toLowerCase()
    }

    getPascalCase() {
        let string_list = this.state.value.split(' ')
        let result = []
        if (string_list.length > 0){
            string_list.forEach(element => {
                if (element.length > 1){
                    result.push(element[0].toUpperCase()+element.slice(1))
                }
            });
        }
        return result.join('')
    }

    getCamelCase() {
        let string_list = this.state.value.split(' ')
        let result = []
        if (string_list.length > 0){
            string_list.forEach((element, index) => {
                if (index == 0){
                    if (element.length > 1){
                        result.push(element.toLowerCase())
                    }
                }else{
                    if (element.length > 1){
                        result.push(element[0].toUpperCase()+element.slice(1))
                    }
                }
            });
        }
        return result.join('')
    }

    getSnakeCase() {
        let string_list = this.state.value.split(' ')
        let result = []
        if (string_list.length > 0){
            string_list.forEach((element) => {
                if (element.length > 1){
                    result.push(element.toLowerCase())
                }
            });
        }
        return result.join('_')
    }

    getKebabCase() {
        let string_list = this.state.value.split(' ')
        let result = []
        if (string_list.length > 0){
            string_list.forEach((element) => {
                if (element.length > 1){
                result.push(element.toLowerCase())
                }
            });
        }
        return result.join('-')
    }

    copy(event){
        navigator.clipboard.writeText(event.target.innerHTML)
    }

    render() {
        return (
            <div>
                <input defaultValue={this.state.value} onChange={this.handleChange} autofocus onFocus={e => e.currentTarget.select()} class="form-control"/>
                <hr/>
                <div className="row">
                    <div className="col-6">
                        <label class="label">Upper Case:</label>
                        <p class="text-muted copy" onClick={this.copy} >{this.getUpperCase()}</p>
                    </div>
                    <div className="col-6">
                        <label class="label">Lower Case:</label>
                        <p class="text-muted copy" onClick={this.copy} >{this.getLowerCase()}</p>
                    </div>
                    <div className="col-6">
                        <label class="label">Pascal Case:</label>
                        <p class="text-muted copy" onClick={this.copy} >{this.getPascalCase()}</p>
                    </div>
                    <div className="col-6">
                        <label class="label">Camel Case:</label>
                        <p class="text-muted copy" onClick={this.copy} >{this.getCamelCase()}</p>
                    </div>
                    <div className="col-6">
                        <label class="label">Snake Case:</label>
                        <p class="text-muted copy" onClick={this.copy} >{this.getSnakeCase()}</p>
                    </div>
                    <div className="col-6">
                        <label class="label">Kebab Case:</label>
                        <p class="text-muted copy" onClick={this.copy} >{this.getKebabCase()}</p>
                    </div>
                </div>
            </div>
        );
    }
}

const domContainer = document.querySelector('#app');
ReactDOM.render(cE(LikeButton), domContainer);