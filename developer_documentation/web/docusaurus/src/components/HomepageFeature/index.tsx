import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

import Link from '@docusaurus/Link';


type FeatureItem = {
  title: string;
  description: JSX.Element;
  link: string;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Smart Contracts',
    description: (
      <>
        Leverage the power of EOS, and distributed computing to build your own dApp.
      </>
    ),
    link: 'http://docs.eosnetwork.com/reference/mandel-contracts/classeosiosystem_1_1system__contract.html',
  },
  {
    title: 'Developer Tools',
    description: (
      <>
        Under the hood look at the developer tools to work with the EOS blockchain.
      </>
    ),
    link: '/eosdocs/developer-tools/',
  },
  {
    title: 'Client SDK',
    description: (
      <>
        Bring the power of EOS into your website, or mobile app.
      </>
    ),
    link: '/eosdocs/client-side/',
  },
];

function Feature({title, description, link}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center padding-horiz--md">
          <h3>{title}</h3>
          <p>{description}</p>
          <div className={styles.buttons}>
            <Link
              className="button button--secondary button--lg"
              to={link}>
              {title}
            </Link>
          </div>
        </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
