import React from "react"
import axios from "axios"

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class App extends React.Component {
	state = {
		details: [],
	};

	componentDidMount() {
		let data

		axios
			.get("http://localhost:8000/sample/")
			.then((res) => {
				data = res.data
				this.setState({
					details: data,
				})
			})
			.catch((err) => { })
	}

	render() {
		return (
			<div>
				{this.state.details.map((detail, id) => (
					<div key={id}>
						<p>
							<span style={{ fontWeight: 'bold' }}>id:</span> {detail.id},
							<span style={{ fontWeight: 'bold' }}> name:</span> {detail.name},
							<span style={{ fontWeight: 'bold' }}> detail:</span> {detail.detail}
						</p>
					</div>
				))}
			</div>
		)
	}
}

export default App
