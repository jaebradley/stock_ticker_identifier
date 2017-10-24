# Stock Ticker Identifier API

## Introduction

There are plenty of APIs that can map a stock ticker to company metadata but it's actually really hard to find an API
that delivers a mapping of a company's name to it's stock ticker.

However, the [NASDAQ](http://www.nasdaq.com/symbol/?Load=true) has a mapping (via CSV files) of [all companies and their
tickers on the NASDAQ, NYSE, and AMEX](http://www.nasdaq.com/screening/company-list.aspx).

## API

### [REST](https://stock-ticker-identifier.herokuapp.com)

#### `/exchanges`
* `GET`
* Query Parameters
    * `search`
        * Searches for `Exchange` names that match the input string
    * `limit`
        * Default value is `10`
    * `offset`
        * Maximum value is `100`

#### `/exchange/{id}`
* `GET`
* No query parameters, but takes an `Exchange` `id` parameter in the URL

#### `/industries`
* `GET`
* Query Parameters
    * `search`
        * Searches for `Industry` names that match the input string
    * `limit`
        * Default value is `10`
    * `offset`
        * Maximum value is `100`

#### `/industry/{id}`
* `GET`
* No query parameters, but takes an `Industry` `id` parameter in the URL

#### `/sectors`
* `GET`
* Query Parameters
    * `search`
        * Searches for `Sector` names that match the input string
    * `limit`
        * Default value is `10`
    * `offset`
        * Maximum value is `100`

#### `/sector/{id}`
* `GET`
* No query parameters, but takes a `Sector` `id` parameter in the URL


#### `/companies`
* `GET`
* Query Parameters
    * `search`
        * Searches for `Industry` names that match the input string
    * `limit`
        * Default value is `10`
    * `offset`
        * Maximum value is `100`

#### `/company/{id}`
* `GET`
* No query parameters, but takes a `Company` `id` parameter in the URL

### [GraphQL Endpoint](https://stock-ticker-identifier.herokuapp.com/graphql)
* [GraphQL Documentation](http://graphql.org/)
* [Graphiql](https://github.com/graphql/graphiql)

#### `AllCompaniesQuery`

![alt-text](https://i.imgur.com/yZ4r4Ba.png)


