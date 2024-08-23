import React from 'react';

type HomeProps = {
  img: string;
};

const Home: React.FC<HomeProps> = ({ img }) => {
  return (
    <div>
      <img
        height={160}
        width={160}
        src={img}
        alt="pic"
      />
    </div>
  );
};

export default Home;