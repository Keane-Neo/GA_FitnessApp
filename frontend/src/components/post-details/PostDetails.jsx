import AddComment from "./AddComment";
import PostDescription from "./PostDescription";
import PostTags from "./PostTags";

const PostDetails = () => {
  return (
    <div>
      <h2>Title of post</h2>
      <PostTags />
      <PostDescription />
      <AddComment />
    </div>
  );
};

export default PostDetails;
