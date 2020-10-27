const express = require("express");
const router = express.Router();

// GET all accounts
router.get("/", async (req, res) => {
  try {
    const item = await Item.find();
    res.json(item);
  } catch (err) {
    res.status(400).json({ message: err });
  }
});

// GET single item (based on id)
router.get("/:accountName", async (req, res) => {
  try {
    const item = await Item.findById(req.params.accountName);
    res.json(item);
  } catch (err) {
    res.status(400).json({
      error: `No account found with id#${req.params.accountName} (error ${err})`,
    });
  }
});

// patch single item (based on id)
router.patch("/:accountName", async (req, res) => {
  const updateField = {};
  if (req.body.active) {
    updateField.user = req.body.user;
  }
  if (req.body.iterations) {
    updateField.mediaUrl = req.body.mediaUrl;
  }
  if (req.body.tags) {
    updateField.category = req.body.category;
  }
  try {
    const updatedItem = await Item.updateOne(
      { _id: req.params.itemID },
      { $set: updateField }
    );
    res.status(200).json({
      message: `Account ${req.params.accountName} has been updated.`,
    });
  } catch (err) {
    res.status(400).json({
      error: `No Account found for ${req.params.accountName} (error ${err})`,
    });
  }
});

module.exports = router;
