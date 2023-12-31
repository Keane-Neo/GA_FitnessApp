import mongoose from "mongoose";

const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: [true, "Your email address is required"],
    unique: true,
  },
  password: {
    type: String,
    required: [true, "Your password is required"],
  },
  createdAt: {
    type: Date,
    default: new Date(),
  },
  userDetail: { type: mongoose.Schema.Types.ObjectId, ref: "UserDetail" },
});

const User = mongoose.model("User", userSchema);

export default User;
