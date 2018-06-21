import React, { Component } from 'react'

import { render } from 'react-dom'
import { BrowserRouter, HashRouter, Route, Switch, Link } from 'react-router-dom'

import querystring from 'query-string'
import formatDateTime from 'date-fns/format'


class Order extends Component {

  constructor(props) {
    super(props)
    this.state = {
      loading: true,
      order: null,
      menu: []
    }
  }

  componentDidMount() {
    this.fetchOrder()

    fetch(`/api/v1/shops/1`)
      .then(resp => resp.json())
      .then(shop => {
        this.setState({ menu: shop.drinks })
      })
  }

  fetchOrder() {
    fetch(`/api/v1/orders/${this.props.match.params.id}`)
      .then(resp => resp.json())
      .then(order => {
        this.setState({ order, loading: false })
      })
  }

  handleSubmit(e) {
    e.preventDefault()

    const form = new FormData(e.target)
    form.append('order', this.state.order.id)

    fetch('/api/v1/items', {
      method: 'POST',
      body: form
    }).then(resp => resp.json())
      .then(_ => this.fetchOrder())

    /* fetch('/api/v1/items', {
     *   method: 'POST',
     *   body: JSON.stringify({
     *     name: e.target.name.value,
     *     drink: e.target.drink.value
     *   }),
     *   headers: {
     *     'Content-Type': 'application/json'
     *   }
     * }).then(resp => resp.json()) */
  }

  render() {
    const { loading, order, menu } = this.state

    if (loading) {
      return (
        <h4>Loading...</h4>
      )
    }

    const summary = order.items.reduce((summary, item) => {
      if (!summary[item.drink]) {
        summary[item.drink] = 0
      }
      summary[item.drink] += 1
      return summary
    }, {})

    return (
      <div className="mw7 center">
        <h1>Order: {formatDateTime(order.date, 'DD/MM/YYYY')}</h1>

        {order.status === 'Open' && (
           <form className="w-100 pv2 flex" onSubmit={e => this.handleSubmit(e)}>
             <input name="name" type="text" placeholder="Name" className="pa2 f5 w-40" />
             <select name="drink" className="ml2 pa2 f4">
               {menu.map(item => (
                 <option value={item.id} key={item.id}>{item.name}</option>
               ))}
             </select>
             <button className="bg-blue white input-reset ml2 pa2">Submit</button>
           </form>
        )}

        <div className="flex">
          <table className="w-60">
            <thead>
              <tr>
                <th className="tl pa2 w-10 bb b--gray">#</th>
                <th className="tl pa2 w-40 bb b--gray">Name</th>
                <th className="tl pa2 w-50 bb b--gray">Drink</th>
              </tr>
            </thead>

            <tbody>
              {order.items.map((item, i) => (
                <tr key={item.id}>
                  <td className="pa2">{i + 1}</td>
                  <td className="pa2">{item.name}</td>
                  <td className="pa2">{item.drink}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <div className="w-40 pa3 bg-near-white">
            <h4 className="mt-0">Summary:</h4>
            <table>
              <thead>
                <tr>
                  <th className="pa2 tl">Drink</th>
                  <th className="pa2 tl">Number</th>
                </tr>
              </thead>
              <tbody>
                {Object.keys(summary).map(drink => (
                  <tr key={drink}>
                    <td className="pa2">{drink}</td>
                    <td className="pa2">{summary[drink]}</td>
                  </tr>
                ))}
                <tr>
                  <td className="pa2"><strong>Total:</strong></td>
                  <td className="pa2">{order.total}<sup>đ</sup></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    )
  }
}

class App extends Component {

  render() {
    return (
      <div>
        <Link to="/order/1">Order 1</Link>
        <Route path="/order/:id" component={Order} />
      </div>
    )
  }
}

render((
  <BrowserRouter>
    <App />
  </BrowserRouter>
), document.querySelector('#app'))
