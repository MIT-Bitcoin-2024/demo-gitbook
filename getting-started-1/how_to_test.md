---
hidden: true
---

# 👨‍💻 HOW\_TO\_TEST

## :exclamation:<mark style="background-color:red;">Disclaimer</mark> :exclamation:

!!! warning "Beta Version" This project is currently in beta and under active development. The testing process described in this document may change frequently as we make updates and improvements.

If you have any questions or would like to discuss potential contributions, please email us at  [founders@lightningbounties.com](mailto:founders@lightningbounties.com).

***

## 🧪 How to Test 👨‍🔬

1. **Fork the Repository and Clone it**
   * Fork the repository on GitHub.
   * Clone the forked repository to your local machine.
2. **Modify the Code**
   * Open the `src/main.py` file and make the desired changes to reflect your modifications.
3. **Generate a Lightning Invoice**
   * Generate a lightning invoice for the payment.
   * Copy the invoice string into the `reward.txt` file.
4. **Commit and Submit a Pull Request**
   * Add and commit your changes to the local repository.
   * Submit a pull request to the base repository.
5. **Pay the Invoice**
   * A GitHub action will be triggered to request a "dust" payment from you (the contributor) to the base repository (the owner).
   * Choose the action that says "Please pay the invoice: lnbc10n1..." (not the one that says "Extracted values:...").
   * Wait for the payment confirmation.
   * Once the payment is confirmed, you'll receive a message saying "Thank you for your payment!"
6. **Request a Reviewer**
   * Ask for a reviewer to review your pull request.
   * Choose either Enrique or Will for this test.
7. **Review and Analysis**
   * After a few seconds, a new action will run.
   * It will first say "Payment has been received, sit tight, running openai query."
   * Approximately 30 seconds later, it will return with a summary of your changes and a security vulnerability analysis.
8. **Merging the Pull Request**
   * We'll keep an eye out for your pull request and attempt to merge it for you.&#x20;
     * As a contributor, you don't have the power to merge it yourself.

**Alternatively:** If you prefer to replicate our work in your own repository:

* Copy the contents of the `.github/` directory into your repository.
* Modify the `main.py` file accordingly.
* Set up the following secrets in your repository settings:
  * `OPENAI_API_KEY`
  * `PAY_INVOICE_KEY` (admin key for LNBits)
  * `WALLET_API_KEY` (invoice/read key for LNBits)
  * `WALLET_BASE_URL` (URL for your LNBits instance)  &#x20;

***

## :map: Lightning Bounties - Join Our Journey! :compass:

:satellite\_orbital:We're excited to share our progress and invite you to join our waitlist for our launch on _<mark style="background-color:green;">September 1st, 2024.</mark>_ Follow us at [LightningBounties.com](https://lightningbounties.com) to stay updated on our journey. :calendar\_spiral:

:rocket:**To be a part of something revolutionary, join us today!** :statue\_of\_liberty:

:milky\_way:**Let's shape the future of open-source development together** :man\_astronaut:



