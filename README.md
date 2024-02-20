# Anime Quotes Database

<p align="center">
<img src="https://i.pinimg.com/originals/35/35/00/3535009c4a5e1d6c611dc436183b2be3.gif" alt="Anime GIF" style="width:50%">
</p>

Welcome to the Anime Quotes Database! 🌟 This repository houses a collection of motivational anime quotes, along with the respective anime names and images.

### Example:

```json

   {
"quotes": [
  {
    "quote": "In The End, You Choose What You Choose.",
    "animeName": "Attack on Titan",
    "image": "https://i.pinimg.com/originals/3c/64/57/3c64570ebe8915e1114c7581536b29b8.gif"
  },
  {
    "quote": "If You Hesitate For So Much As A Second, You'll Be Dead. The Moment You See An Opening, Go For The Kill..",
    "animeName": "Attack on Titan",
    "image": "https://pop-wrapped.s3-us-west-1.amazonaws.com/articles/81872/live-action-cast-attack-titan-unveiled-costume-1-med.gif"
  },
  {
    "quote": "It Doesn't Matter How Strong The Opposition Is. It Doesn't Matter How Fearsome The World Is, It Doesn't Matter How Cruel The World Is. Fight!",
    "animeName": "Attack on Titan",
    "image": "https://static1.srcdn.com/wordpress/wp-content/uploads/2021/03/Eren-in-Attack-on-Titan.jpg?q=50&fit=crop&w=500&dpr=0.5"
  }
]
}

```

## How to Contribute

We welcome contributions to enhance our database with more inspirational quotes from various anime series. Follow these steps to contribute:

1. Fork the repository.

2. Clone your forked repository to your local machine:

   ```bash
   git clone https://github.com/SanskritiGupta05/AniQuotes
   ```

3. Open the `db.json` file in your preferred text editor. This file contains the quotes, anime names, and images.

4. Add a new quote:

   - Find the existing quotes and follow the same structure.
   - Ensure the JSON syntax is valid.

     ```json
     {
       "quote": "Your new motivational anime quote.",
       "animeName": "Name of the anime",
       "image": "URL to a live image or GIF related to the quote or anime (not too large in size)"
     },
     ```

   - **Note:** The image must not be very large in size, and it must be a live image link (URL) rather than a static upload. GIFs are also welcome!
   - **PLEASE Make sure the quote you are adding has not already been added to the Database!!**

or

5. Run the script `add_quote.py`
   ```bash
   python3 add_quote.py
   ```

6. Add a new quote

   ![Screenshot 2024-02-19 222742](https://github.com/levo-777/AniQuotes/assets/148566093/3d5e6bfc-27c4-4f98-9fcf-7a4a46b55c8f)


7. Save the changes
   
8. Commit your changes:

   ```bash
   git add db.json
   git commit -m "Add new motivational anime quote"
   ```

9. Push your changes to your GitHub repository:

   ```bash
   git push origin main
   ```

10. Create a Pull Request:

   - Go to the [original repository](https://github.com/SanskritiGupta05/AniQuotes).
   - Click on "Pull Requests" and then "New Pull Request."
   - Choose the branch with your changes.

11. Wait for your Pull Request to be reviewed and merged. Feel free to discuss and make any necessary changes as suggested by the maintainers.

Thank you for contributing to the Anime Quotes Database! Your contributions make this collection more diverse and inspirational.

## Image Requirements

- The image must not be very large in width/height.
- It must be a live image link (URL) rather than a static upload.
- GIFs are also welcome!

## Usage

The quotes from this database are used in the [Anime Motivation Chrome Extension](https://github.com/SanskritiGupta05/AniQuotes-Chrome-Extension/tree/main). Feel free to check it out and contribute to both projects.

## Code of Conduct

Please note that by contributing to this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Ensure a positive and inclusive environment for everyone.

---

**Anime Quotes Database** is maintained by [Sanskriti Gupta](https://github.com/SanskritiGupta05).
