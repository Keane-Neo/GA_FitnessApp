import mongoose from "mongoose";

const userDetailSchema = new mongoose.Schema({
  name: {
    type: String,
  },
  username: {
    type: String,
    required: [true, "Your username is required"],
    unique: true,
  },
  age: {
    type: Number,
  },
  gender: {
    type: String,
  },
  userType: {
    type: String,
    required: [true, "Select a user type"],
  },
  bio: {
    type: String,
  },
  avatarUrl: {
    type: String,
  },
  clients: [{ type: mongoose.Schema.Types.ObjectId, ref: "UserDetail" }],
});

userDetailSchema.index({
  username: "text",
});

const UserDetail = mongoose.model("UserDetail", userDetailSchema);

export default UserDetail;
