# Ups0authClientCredentials Python SDK 1.0.0

Welcome to the Ups0authClientCredentials SDK documentation. This guide will help you get started with integrating and using the Ups0authClientCredentials SDK in your project.

## Versions

- SDK version: `1.0.0`

## About the API

The UPS OAuth Client Credentials API helps retrieve an OAuth Bearer token when the integration owner is also the UPS shipper. The integration owner uses their UPS login credentials, and the UPS account number, to receive a token that can be used in the authorization HTTP header of subsequent API calls to UPS APIs like the Ship API, Track API, etc. https://developer.ups.com/api/reference/oauth/client-credentials

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [Basic Authentication](#basic-authentication)
- [Services](#services)
- [Models](#models)
- [License](#license)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install ups-0auth-client-credentials
```

## Authentication

### Basic Authentication

The Ups0authClientCredentials API uses Basic Authentication.

You need to provide your username and password when initializing the SDK.

#### Setting the Username and Password

When you initialize the SDK, you can set the username and password as follows:

```py
Ups0authClientCredentials(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD"
)
```

If you need to set or update the username and password after initializing the SDK, you can use:

```py
sdk.set_basic_auth("YOUR_USERNAME", "YOUR_PASSWORD")
```

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                         |
| :----------------------------------------------------------- |
| [SecurityService](documentation/services/SecurityService.md) |

</details>

## Models

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models with links to their detailed documentation:</summary>

| Name                                                                 | Description |
| :------------------------------------------------------------------- | :---------- |
| [CreateTokenRequest](documentation/models/CreateTokenRequest.md)     |             |
| [TokenSuccessResponse](documentation/models/TokenSuccessResponse.md) |             |

</details>

## License

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.

<!-- This file was generated by liblab | https://liblab.com/ -->
