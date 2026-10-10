# Second-ring extract: Google Search Central and Help pages

All pages fetched 2026-10-10. Raw HTML in `raw/<name>.html`, plain text in `<name>.txt` in this folder.
Labels: MUST (required), SHOULD (recommended), NEVER (prohibition), N/A (does not apply to a small editorial publisher site, with the reason).
Bullets quote the source wording. Nothing here is advice from us.

Fetch notes: pages 7, 8 and 9 (sitelinks search box, FAQ, how-to) no longer exist; each URL answers with a 301 redirect to https://developers.google.com/search/updates, so their extracts hold the changelog entries only. The full changelog is saved as `updates-page.txt`. Every other page rendered as text.

---

## 1. Google Search technical requirements
URL: https://developers.google.com/search/docs/essentials/technical  | Fetched: 2026-10-10 | Page says "Last updated 2025-12-18 UTC" | File: technical.txt

- MUST: "Googlebot isn't blocked."
- MUST: "The page works, meaning that Google receives an HTTP 200 (success) status code."
- MUST: "The page has indexable content."
- Note: "Just because a page meets these requirements doesn't mean that a page will be indexed; indexing isn't guaranteed."
- NEVER (page not indexed): "If a page is made private, such as requiring a log-in to view it, Googlebot will not crawl it."
- Note: "Pages that are blocked by robots.txt are unlikely to show in Google Search results."
- Note: "Client and server error pages aren't indexed."
- MUST: indexable content means "The textual content is in a file type that Google Search supports." and "The content doesn't violate our spam policies."
- MUST: "While blocking Googlebot with a robots.txt file will prevent crawling, a page's URL might still appear in search results. To instruct Google not to index a page, use noindex and allow Google to crawl the URL."
- SHOULD: "Check if Googlebot can find and access your page": "use both the Page Indexing report and Crawl Stats report in Search Console"; "To test a specific page, use the URL Inspection tool."

## 2. Content policies for Google Search
URL: https://support.google.com/websearch/answer/10622781  | Fetched: 2026-10-10 | Rendered as text: yes | File: content-policies.txt

Overall content policies (apply to web results):
- NEVER: "Child sexual abuse imagery or exploitation material": "We block search results that lead to child sexual abuse imagery or material that appears to victimize, endanger, or otherwise exploit children."
- NEVER: "Highly personal information": "doxxing content, explicit personal images, and involuntary fake pornography" may be removed.
- NEVER: "Spam": "techniques used to deceive users or manipulate our Search systems into ranking content highly." Consequence: "We issue a manual action against a site after Google human reviewers determine that its pages are engaged in spam".
- Consequence: "We may manually remove content that goes against Google's content policies" and "We may also demote sites, such as when we find a high volume of policy content violations within a site."
- N/A: "Valid legal requests" (DMCA, local law, Right to be Forgotten): these are Google's removals on notice, not a publisher action. Quote: "we remove content if we receive valid notification under the US Digital Millennium Copyright Act (DMCA)."
- N/A: "Webmaster & site owner requests": a removal route for the owner, not a requirement.

Search features policies ("These policies apply to many of our search features... enhancements to web listings (such as through structured data)... These policies don't apply to web results."):
- NEVER: "Advertisements": "We don't allow content that primarily advertises products or services, which includes direct calls to purchase, links to other websites, company contact information, and other promotional tactics. We don't allow sponsored content that's concealed or misrepresented as independent content."
- NEVER: "Deceptive practices": "We don't allow content or accounts that impersonate any person or organization, misrepresent or hide ownership or primary purpose, or engage in false or coordinated behavior to deceive, defraud, or mislead."
- NEVER: "Working together in ways that conceal or misrepresent information about relationships or editorial independence."
- NEVER: "Misrepresentation or concealment of country of origin, government or political interest group affiliation." and "Directing content to users in another country under false premises."
- Exception: "This policy doesn't cover content with certain artistic, educational, historical, documentary, or scientific considerations, or other substantial benefits to the public."
- NEVER: "Dangerous content": "content that could directly facilitate serious and immediate harm to people or animals."
- NEVER: "Harassing content": "harassment, bullying, or threatening content" (single out for malicious abuse, threaten, sexualize, expose private information, disparage victims, deny an atrocity).
- NEVER: "Hateful content": "content that promotes or condones violence, promotes discrimination, disparages or has the primary purpose of inciting hatred against a group."
- NEVER: "Manipulated media": "audio, video, or image content that's been manipulated to deceive, defraud, or mislead by means of creating a representation of actions or events that verifiably didn't take place."
- NEVER: "Medical content": "content that contradicts or runs contrary to scientific or medical consensus and evidence-based best practices."
- NEVER: "Sexually explicit content": "nudity, graphic sex acts, or sexually explicit material. Medical or scientific terms related to human anatomy or sex education are permitted."
- NEVER: "Violent extremist content" and "Violent & gory content" ("shocking, sensational, or gratuitous").
- NEVER: "Vulgar language & profanity": "obscenities or profanities that are primarily intended to be shocking, sensational, or gratuitous."
- Feature-specific policy pages listed: Autocomplete, Dictionary boxes, Featured snippets, Google Discover, Google News, Google Podcasts, Image & video boxes, Knowledge Graph & Knowledge Panels, Product listings, Structured data, Structured data for job postings, User content on Search, Web Story Content Policies.
- N/A: Podcasts, job postings, Web Stories pages are only listed here, not extracted, and do not apply to the site.

## 3. Breadcrumb (BreadcrumbList) structured data
URL: https://developers.google.com/search/docs/appearance/structured-data/breadcrumb  | Fetched: 2026-10-10 | Page says "Last updated 2026-09-08 UTC" | File: breadcrumb.txt

- Availability: "This feature is available on desktop in all regions and languages where Google Search is available."
- MUST: "You must follow these guidelines to be eligible to appear with breadcrumbs in Google Search": Search Essentials and General structured data guidelines.
- NEVER: "If Google detects that some of the markup on your pages may be using techniques that are outside our structured data guidelines, your site may receive a manual action."
- SHOULD: "We recommend providing breadcrumbs that represent a typical user path to a page, instead of mirroring the URL structure."
- Note: "It is not required to include a breadcrumb ListItem for the top level path (your site's domain or host name), nor for the page itself."
- MUST: "define a BreadcrumbList that contains at least two ListItems. You must include the required properties for your content to be eligible for display with breadcrumbs."
- Multiple trails: "If there are multiple ways to navigate to a page on your site, you can specify multiple breadcrumb trails for a single page."
- NEVER: "Data-vocabulary.org markup is no longer eligible for Google rich result features."
- BreadcrumbList required: itemListElement (ListItem), "An array of breadcrumbs listed in a specific order."
- ListItem required: item, "URL or a subtype of Thing", "The URL to the webpage that represents the breadcrumb." Exception: "If the breadcrumb is the last item in the breadcrumb trail, item is not required. If item isn't included for the last item, Google uses the URL of the containing page."
- ListItem required: name (Text), "The title of the breadcrumb displayed for the user. If you're using a Thing with a name instead of a URL to specify item, then name is not required."
- ListItem required: position (Integer), "Position 1 signifies the beginning of the trail."
- Recommended properties: none listed on the page.
- SHOULD: "Validate your code using the Rich Results Test and fix any critical errors." Non-critical issues: "this isn't necessary to be eligible for rich results".
- SHOULD: "Deploy a few pages that include your structured data and use the URL Inspection tool to test how Google sees the page", and "we recommend that you submit a sitemap."
- SHOULD: Search Console checks: "After deploying structured data for the first time", "After releasing new templates or updating your code", "Analyzing traffic periodically."
- Note: "Google does not guarantee that features that consume structured data will show up in search results."
- Note: "If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results)."

## 4. Organization structured data
URL: https://developers.google.com/search/docs/appearance/structured-data/organization  | Fetched: 2026-10-10 | Page says "Last updated 2026-09-08 UTC" | File: organization.txt

- Purpose: "Adding organization structured data to your home page can help Google better understand your organization's administrative details and disambiguate your organization in search results."
- Required properties: "There are no required properties; instead, we recommend adding as many properties that are relevant to your organization."
- MUST: "You must follow these guidelines to enable structured data to be eligible for inclusion in Google Search results": Technical guidelines, Search Essentials, General structured data guidelines.
- NEVER: "If your site violates one or more of these guidelines, then Google may take manual action against it."
- SHOULD: "We recommend placing this information on your home page, or a single page that describes your organization, for example the about us page. You don't need to include it on every page of your site."
- SHOULD: "We recommend using the most specific schema.org subtype of Organization that matches your organization."
- SHOULD: "We recommend focusing on properties that are useful to your users, such as name or alternateName for your business name as well as an indication of real-world presence (for example, address or telephone) and online presence (for example, url or logo)."
- Recommended properties exactly as listed: address (PostalAddress; addressCountry, addressLocality, addressRegion, postalCode, streetAddress), alternateName, contactPoint (ContactPoint; contactPoint.email, contactPoint.telephone), description, duns, email, foundingDate, globalLocationNumber, hasMerchantReturnPolicy, hasMemberProgram, hasShippingService, iso6523Code, legalName, leiCode, logo, naics, name, numberOfEmployees, sameAs, taxID, telephone, url, vatID.
- name: "The name of your organization. Use the same name and alternateName that you're using for your site name."
- logo: "The image must be 112x112px, at minimum."; "The image URL must be crawlable and indexable."; "The image file format must be supported by Google Images."; "Make sure the image looks how you intend it to look on a purely white background".
- logo (ImageObject): "make sure that it has a valid contentUrl property or url property".
- url: "The URL of the website of your organization, if applicable. This helps Google uniquely identify your organization."
- sameAs: "The URL of a page on another website with additional information about your organization, if applicable... You can provide multiple sameAs URLs."
- legalName: "The registered, legal name of your Organization, if applicable and different from the name property."
- N/A: hasMerchantReturnPolicy, hasShippingService, hasMemberProgram, duns, naics, taxID, vatID, numberOfEmployees, globalLocationNumber: merchant and business-registry fields; the site does not sell physical goods (the books section is affiliate links).
- Note: "Google does not guarantee that features that consume structured data will show up in search results."

## 5. Profile page (ProfilePage) structured data
URL: https://developers.google.com/search/docs/appearance/structured-data/profile-page  | Fetched: 2026-10-10 | File: profile-page.txt

- Purpose: "ProfilePage markup is designed for any site where creators (either people or organizations) share first-hand perspectives."
- MUST: "you must follow these guidelines": General structured data guidelines, Search Essentials, Content Guidelines, Technical Guidelines.
- MUST (content): "The primary focus of the page must be a single person or organization that is affiliated with the overall website."
- Valid use cases: "An author page on a news site"; "An 'About Me' page on a blog site"; "A user profile page on a forum or social media site"; "An employee page on a company website".
- NEVER (invalid use cases): "The main home page of a store (usually contains lots of non-profile info)"; "An organization review site (the organization isn't associated with the website)".
- Technical: "If the profile page also includes the creator's recent activity, you can include markup using URLs on those objects to reference the page with the full content and markup."
- ProfilePage required: mainEntity (Person or Organization), "The person or organization that this profile page is about." "Try to use the correct type if that information is available... otherwise, default to Person".
- ProfilePage recommended: dateCreated (DateTime, ISO 8601), dateModified (DateTime, ISO 8601; "Ideally, this only represents human-edited metadata changes to the profile").
- Person or Organization required: name (Text), "We recommend using this field for real names (and alternateName for social media handles)." "If the name property isn't available, you can provide the alternateName property to fulfill this requirement."
- Person or Organization recommended: agentInteractionStatistic, alternateName, description ("The user's byline or applicable credential"), identifier, image, interactionStatistic, sameAs.
- image: "If there are no images, don't include a default image, icon, or placeholder image in this field." Also: "Image URLs must be crawlable and indexable."; "Images must represent the marked up content."; "Images must be in a file format that's supported by Google Images."; "For best results, we recommend providing multiple high-resolution images (minimum of 50K pixels when multiplying width and height) with the following aspect ratios: 16x9, 4x3, and 1x1."
- interactionStatistic: "Only include stats about the platform that the profile page is hosted on (don't reference that the creator also has 100,000 followers on their home page)."
- sameAs: "The URL to other external profiles or home pages for the profile, if applicable."
- N/A: agentInteractionStatistic and interactionStatistic (follow, like, write, share counts): a one-author site has no community activity to count.
- Note: "Other structured data features can link to pages with ProfilePage markup too. For example, Article and Recipe structured data have authors".

## 6. Site names
URL: https://developers.google.com/search/docs/appearance/site-names  | Fetched: 2026-10-10 | Page says "Last updated 2025-12-10 UTC" | File: site-names.txt

- Availability: "Site names are available in all languages where Google Search is available, on both mobile and desktop."
- Note: "Google's generation of site names on the Google Search results page is completely automated and takes into account content from a site's home page and references to it that appear on the web."
- SHOULD: "To indicate your site name preference, add WebSite structured data to your home page." Also "Our site name system will also consider content in og:site_name... structured data is most important, if you want to specify a preference."
- Note: "While we can't manually change automatically selected site names, you can indicate alternatives".
- Choosing a name:
  - SHOULD: "Choose a unique name that accurately reflects the identity of your site and isn't misleading for users. The name you choose must follow Search content policies."
  - SHOULD: "Use a concise, commonly-recognized name for your site... long site names may be truncated on some devices."
  - SHOULD: "Avoid using a generic name."
  - SHOULD: "Use your site name consistently across your home page. Make sure whatever you use as the site name in structured data is consistent with how you refer to your site in other sources on your home page that our system considers."
  - SHOULD: "Provide an alternative name" with the alternateName property.
- Technical guidelines:
  - MUST: "Only one name per site": "Google Search does not support site names at the subdirectory level." "subdomain names starting with www or m are generally considered as being equivalent."
  - MUST: "The WebSite structured data must be on the home page of the site. By home page, we mean the domain or subdomain level root URI."
  - MUST: "The home page must be crawlable by Google".
  - SHOULD: "If you have duplicate home pages for the same content (for example, HTTP and HTTPS versions of your home page, or www and non-www), make sure that you're using the same structured data on all page duplicates, not just on the canonical page."
  - SHOULD: "If you already have WebSite structured data on your site, make sure that you nest the site name properties in the same node... avoid creating an additional WebSite structured data block on your home page if you can help it."
- Required properties: name (Text) "The name of the website."; url (URL) "Set this to the canonical home page of your site's domain or subdomain."
- Recommended property: alternateName (Text), "You can list more than one alternative name. Specify them in order of your preference, with the most important one listed first."
- Note: "You don't need to include this markup on every page of your site; you only need to add this markup to the home page of your site."
- Testing: "Site names aren't supported in the Rich Results Test." Use "a schema testing tool (for example, Schema Markup Validator)" and the URL Inspection tool.
- If not selected: "Provide your domain or subdomain name as a backup option... Your domain or subdomain needs to be in all lowercase"; last resort "providing your domain or subdomain name (in all lowercase) as your preferred name".

## 7. Sitelinks search box
URL: https://developers.google.com/search/docs/appearance/structured-data/sitelinks-searchbox  | Fetched: 2026-10-10 | File: sitelinks-searchbox.txt

- Page failed to render: the URL redirects to https://developers.google.com/search/updates#bye-sitelinkbox.
- Changelog (November 29, 2024): "Removed the sitelinks search box documentation and archived the nositelinkssearchbox rule." "The sitelinks search box feature is no longer available in Google Search results."
- Robots meta page confirms: "The nositelinkssearchbox rule is no longer used by Google Search to control whether the sitelink search box is shown for a given page, as the feature no longer exists."
- N/A: feature no longer exists.

## 8. FAQPage structured data
URL: https://developers.google.com/search/docs/appearance/structured-data/faqpage  | Fetched: 2026-10-10 | File: faqpage.txt

- Page failed to render: the URL redirects to https://developers.google.com/search/updates#removing-faq-rich-result.
- Changelog (May 8, 2026): "Added a deprecation notice to the FAQ rich result documentation." "This feature will no longer appear in Google Search starting May 7, 2026."
- Changelog (June 2026): "Removed documentation for the FAQ rich result feature." "The FAQ rich result feature is no longer shown in Google Search results".
- Changelog (September 14, 2023): "Updated the FAQ structured data documentation to state that the feature is only shown for well-known, authoritative government and health websites."
- N/A: the FAQ rich result is no longer shown for any site.

## 9. HowTo structured data
URL: https://developers.google.com/search/docs/appearance/structured-data/how-to  | Fetched: 2026-10-10 | File: how-to.txt

- Page failed to render: the URL redirects to https://developers.google.com/search/updates#how-to-deprecation.
- Changelog (September 14, 2023): "Removed the How-to rich result case study, as this feature is deprecated." "Removed the How-to structured data documentation, as this rich result is no longer shown in search results, on both desktop and mobile devices."
- N/A: the HowTo rich result is no longer shown.

## 10. Image metadata in Google Images (image license metadata)
URL: https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata  | Fetched: 2026-10-10 | Page says "Last updated 2025-12-10 UTC" | File: image-license-metadata.txt

- Availability: "available on mobile and desktop, and in all regions and languages that Google Search is available."
- Purpose: "providing licensing information can make the image eligible for the Licensable badge".
- MUST (discovery): "Make sure people can access and view your pages that contain images without needing an account or logging in."
- MUST: "Make sure Googlebot can access your pages that contain images (meaning, your pages aren't disallowed by a robots.txt file or robots meta tag)."
- SHOULD: "Follow the Search Essentials", "Follow the image SEO best practices", "we recommend that you submit a sitemap."
- Method: "add structured data or IPTC photo metadata to each image on your site. If you have the same image on multiple pages, add structured data or IPTC photo metadata to each image on each page that it appears." "You only need to provide Google with one form of information to be eligible for enhancements like the Licensable badge".
- Structured data: "You need to add structured data for every instance an image is used, even if it's the same image."
- IPTC: "You only need to embed IPTC photo metadata once per image."
- Conflict rule: "if any information conflicts between the two, Google will use the structured data information."
- ImageObject required: contentUrl (URL), "Google uses contentUrl to determine which image the photo metadata applies to." "Google also supports the url property... we recommend you use contentUrl instead".
- ImageObject required: "Either creator or creditText or copyrightNotice or license": "In addition to contentUrl, you must include one of the following properties". "Once you include one of these properties, the other three properties become recommended in the Rich Results Test."
- ImageObject recommended: acquireLicensePage (URL), creator (Organization or Person), creator.name (Text), creditText (Text), copyrightNotice (Text), license (URL).
- Licensable badge: "If you're using structured data to specify an image, you must include the license property for your image to be eligible to be shown with the Licensable badge. We recommend that you also add the acquireLicensePage property if you have that information."
- IPTC recommended fields: Copyright Notice, Creator, Credit Line, Digital Source Type, Licensor URL, Web Statement of Rights.
- IPTC Licensable badge: "You must include the Web Statement of Rights field for your image to be eligible to be shown with the licensable badge." "We recommend that you also add the Licensor URL field if you have that information." "The Licensor URL must be a property of a Licensor object, not a property of the image object."
- Digital Source Type values Google supports: "trainedAlgorithmicMedia", "compositeSynthetic", "algorithmicMedia", "compositeWithTrainedAlgorithmicMedia".
- C2PA: "If an image contains C2PA metadata, Google can extract those details and may show information in the" "About this image" feature. Signer conditions: "The app, device, or service has adopted C2PA version 2.1 or later."; "The image's manifest must be signed by a certificate from a Certification Authority on the C2PA Trust List."
- Note: "Google does not guarantee that structured data or IPTC photo metadata will show up in search results."
- SHOULD: "Google recommends that, at the very least, you retain critical metadata related to image rights information and identification. For example, whenever possible try to keep the IPTC fields creator, credit line, and copyright notice to provide proper attribution."
- Warning: "removing metadata may be illegal in certain jurisdictions."
- Note: the page contains no requirement to label AI-made images for Search; it only lists the Digital Source Type values.

## 11. Merchant Center: AI-generated content
URL: https://support.google.com/merchants/answer/14743464  | Fetched: 2026-10-10 | Rendered as text: yes | File: merchant-ai-content.txt

- Scope: Merchant Center product data ("we now require some types of product data to be identified as being AI-generated").
- MUST (Merchant Center only): "All images created using generative AI must contain meta data indicating that the image was AI-generated by using the IPTC DigitalSourceTypeTrainedAlgorithmicMedia metadata tag."
- NEVER (Merchant Center only): "Don't remove embedded metadata tags such as the IPTC DigitalSourceType property from images created using generative AI tools".
- MUST (Merchant Center only): AI-generated titles use the "structured title [structured_title]" attribute with "Digital source type [digital_source_type]" value "trained_algorithmic_media" and "Content [content]".
- MUST (Merchant Center only): "All descriptions created using generative AI must be provided using the structured description [structured_description] attribute", same sub-attributes.
- N/A: applies only to product data submitted to Merchant Center; the site has no product feed (affiliate book links and free template downloads are not Merchant Center products).

## 12. Structured data testing landing page, and Rich Results Test help
URLs: https://developers.google.com/search/docs/appearance/structured-data and https://support.google.com/webmasters/answer/7445569  | Fetched: 2026-10-10 | Files: structured-data-intro.txt, rich-results-test.txt

Note: https://developers.google.com/search/docs/appearance/structured-data returned the short "Test your structured data" landing page. The page that explains how structured data works is already saved as `intro-structured-data.txt`. The Rich Results Test link on the landing page is https://search.google.com/test/rich-results (a tool, not fetched); its help page is 7445569.

From the landing page:
- SHOULD: "Google recommends that you start with the Rich Results Test to see what Google rich results can be generated for your page. For generic schema validation, use the Schema Markup Validator to test all types of schema.org markup, without Google-specific validation."
- Note: "We removed Google-specific validation from the Structured Data Testing Tool and migrated the tool to a new domain, Schema Markup Validator."

From the Rich Results Test help:
- Supported formats: "The Rich Results test supports structured data in JSON-LD, RDFa, and Microdata".
- MUST (to be testable): "All page resources must be accessible by an anonymous user accessing the code from the internet. Any resources that are behind a firewall or password-protected will not be available to the test. If your page is behind a firewall or hosted on your local machine, you can test it by exposing a tunnel."
- Note: "If Google is prevented from crawling the page as part of its regular crawl cycle (for example, is prevented from crawling by a robots.txt rule or noindex directive), the page cannot be tested with this tool."
- SHOULD: "Be sure to remove any comments from JSON-LD before publishing your final page."
- Note: "The default user agent is smartphone".
- Note: "This tool accesses the page as Google-InspectionTool... it can be blocked by a robots.txt file."
- SHOULD: "You should make sure that important resources are not blocked to Google-InspectionTool by robots.txt and are generally accessible."
- MUST (for test to run): "Invalid server SSL certificate: Your site's SSL certificate is invalid. Google won't test an HTTPS URL on the site unless the certificate is valid."
- Supported rich result types listed: Article, Breadcrumb, Carousel, Course list item, Discussion forum, Dataset, Education Q&A, Employer aggregate rating, Event, Hotels, Image metadata, Job posting, Local business, Loyalty program, Math solvers, Movie, Merchant listings, Organization, Paywalled content, Practice Problems, Product snippet, Profile page, Q&A page, Recipe, Return policy, Review snippet, Shipping policies, Software app, Subscribed Content, Vacation rental, Video.
- Not in the supported list: WebSite (site names), FAQ, How-to, Sitelinks search box.
- Note: "Test history is saved for approximately 90 days. These bookmarks are accessible by anyone."
- N/A: pages on a local machine cannot be tested without a tunnel (the quote above).

## 13. Google image SEO best practices
URL: https://developers.google.com/search/docs/appearance/google-images  | Fetched: 2026-10-10 | Page says "Last updated 2026-03-02 UTC" | File: google-images.txt

- SHOULD: "Using standard HTML image elements helps crawlers find and process images. Google can find images in src attribute of <img> element (even when it's a child of other elements, such as the <picture> element)."
- NEVER (not indexed): "Google doesn't index CSS images."
- SHOULD: "You can provide the URL of images we might not have otherwise discovered by submitting an image sitemap." Also: "If you're using a CDN, we encourage you to verify ownership of the CDN's domain name in Search Console".
- SHOULD: responsive images: "We recommend that you always specify a fallback URL using the src attribute." For picture: "make sure that you provide an img element as a fallback with a src attribute".
- Formats: "BMP, GIF, JPEG, PNG, WebP, SVG, and AVIF. It's also a good idea to have the extension of your filename match with the file type."
- Note: Data URIs supported, "carefully judge when to use them since it can considerably increase the size of the page."
- SHOULD: "Make sure to apply the latest image optimization and responsive image techniques to provide a high quality and fast user experience."
- SHOULD (preferred image): "providing your preferred image through one of the following metadata sources": "schema.org primaryImageOfPage", an image property "attached to the main entity (using the schema.org mainEntity or mainEntityOfPage properties)", or "the og:image meta tag".
- SHOULD: "Choose an image that's relevant and representative of the page."
- SHOULD NOT: "Avoid using a generic image (for example, your site logo) or an image with text in the schema.org markup or og:image meta tag."
- SHOULD NOT: "Avoid using an image with an extreme aspect ratio (such as images that are too narrow or overly wide)."
- SHOULD: "Use a high resolution, if possible."
- SHOULD: "You can help us improve the quality of the title link and snippet displayed for your pages by following Google's title and snippet guidelines."
- MUST (for image rich results): "Follow the general structured data guidelines as well as any guidelines specific to your structured data type; otherwise your structured data might be ineligible for rich result display in Google Images." "the image attribute is a required field to be eligible for a badge and rich result in Google Images."
- SHOULD: "Wherever possible, make sure images are placed near relevant text and on pages that are relevant to the image subject matter."
- SHOULD: "use filenames that are short, but descriptive. For example, my-new-black-kitten.jpg is better than IMG00023.JPG. Avoid using generic filenames like image1.jpg, pic.gif, 1.jpg when possible."
- SHOULD: "The most important attribute when it comes to providing more metadata for an image is the alt text".
- SHOULD: "focus on creating useful, information-rich content that uses keywords appropriately and is in context of the content of the page."
- NEVER: "Avoid filling alt attributes with keywords (also known as keyword stuffing) as it results in a negative user experience and may cause your site to be seen as spam."
- Note: "alt text in images is useful as anchor text if you decide to use an image as a link."
- SHOULD: "consistently reference the image with the same URL, so that Google can cache and reuse the image without needing to request it multiple times."
- Optional: opt out of inline linking by answering Google-referrer requests with "a 200 HTTP status code, or a 204 HTTP status code and no content." "This behavior isn't considered image cloaking and won't result in manual actions."
- Note (SafeSearch): "Make sure Google understands the nature of your site so that Google can apply SafeSearch filters to your site if appropriate."

## 14. Canonical URLs (consolidate duplicate URLs)
URL: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls  | Fetched: 2026-10-10 | Page says "Last updated 2026-07-10 UTC" | File: consolidate-duplicate-urls.txt

- Signal strength: "Redirects: A strong signal"; "rel="canonical" link annotations: A strong signal"; "Sitemap inclusion: A weak signal". "these methods can stack".
- Note: "none of them are required; your site will likely do just fine without specifying a canonical preference. That's because if you don't specify a canonical URL, Google will identify which version of the URL is objectively the best version to show to users in Search."
- Note (CMS): "If you use a CMS, such as WordPress, Wix, or Blogger, you might not be able to edit your HTML directly."
- Reasons: "To specify which URL that you want people to see in search results"; "To consolidate signals for similar or duplicate pages"; "To simplify tracking metrics"; "To avoid spending crawling time on duplicate pages."
- NEVER: "Don't use the robots.txt file for canonicalization purposes. Google may still index URLs that are disallowed in robots.txt without their content."
- NEVER: "Don't use the URL removal tool for canonicalization. It hides all versions of a URL from Search."
- NEVER: "Don't specify different URLs as canonical for the same page using different canonicalization techniques".
- NEVER: "Don't specify a URL fragment as canonical".
- SHOULD: "Do include a rel="canonical" link on the canonical page itself (also known as a self-referential canonical)."
- NEVER: "We don't recommend using noindex to prevent selection of a canonical page within a single site, because it will completely block the page from Search. rel="canonical" link annotations are the preferred solution."
- SHOULD: "When linking within your site, link to the canonical URL rather than a duplicate URL."
- SHOULD (JavaScript): "specify the canonical URL in the HTML source code and make sure that JavaScript doesn't change the canonical link element."
- NEVER: "rel="canonical" annotations with hreflang, lang, media, and type attributes are not used for canonicalization."
- SHOULD: "We recommend that you choose one of these [link element or HTTP header] and go with that; while supported, using both methods at the same time is more error prone".
- SHOULD: "Use absolute paths rather than relative paths with the rel="canonical" link element."
- MUST: "The rel="canonical" link element is only accepted if it appears in the <head> section of the HTML".
- Sitemap: "Pick a canonical URL for each of your pages and submit them in a sitemap. All pages listed in a sitemap are suggested as canonicals".
- Redirects: "Use this method when you want to get rid of existing duplicate pages." "For the quickest effect, use HTTP (also known as server-side) redirects."
- HTTPS: "Google prefers HTTPS pages over equivalent HTTP pages as canonical, except when there are issues": invalid SSL certificate; insecure dependencies (other than images); "The HTTPS page redirects users to or through an HTTP page."; "The HTTPS page has a rel="canonical" link to the HTTP page."
- SHOULD: "Add redirects from the HTTP page to the HTTPS page." "Add a rel="canonical" link from the HTTP page to the HTTPS page." "Implement HSTS."
- NEVER: "Avoid bad TLS/SSL certificates and HTTPS-to-HTTP redirects because they cause Google to prefer HTTP very strongly."
- NEVER: "Don't include the HTTP version of your pages in your sitemap or hreflang annotations rather than the HTTPS version."
- NEVER: "Avoid implementing your SSL/TLS certificate for the wrong host-variant."
- N/A: HTTP header canonical (for non-HTML files such as PDF) matters only if template downloads are served as files on their own URLs. AMP variant, hreflang clusters: no AMP or multilingual set.

## 15. Sitemaps overview
URL: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview  | Fetched: 2026-10-10 | Page says "Last updated 2025-12-10 UTC" | File: sitemaps-overview.txt

- Note: "If you're using a CMS such as WordPress, Wix, or Blogger, it's likely that your CMS has already made a sitemap available to search engines and you don't have to do anything."
- Note: "A sitemap helps search engines discover URLs on your site, but it doesn't guarantee that all the items in your sitemap will be crawled and indexed. However, in most cases, your site will benefit from having a sitemap."
- You might need one if: "Your site is large"; "Your site is new and has few external links to it"; "Your site has a lot of rich media content (video, images) or is shown in Google News."
- You might not need one if: "Your site is 'small'. By small, we mean about 500 pages or fewer on your site. Only pages that you think need to be in search results count toward this total."; "Your site is comprehensively linked internally"; "You don't have many media files (video, image) or news pages".
- Definition of proper linking: "all pages that you deem important can be reached through some form of navigation, be that your site's menu or links that you placed on pages."
- Information a sitemap can carry: "when the page was last updated and any alternate language versions of the page."
- SHOULD (from other pages): "submit a sitemap" (structured data and image pages).

## 16. Robots meta tag, data-nosnippet and X-Robots-Tag
URL: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag  | Fetched: 2026-10-10 | Page says "Last updated 2026-03-24 UTC" | File: robots-meta-tag.txt

- MUST: "these settings can be read and followed only if crawlers are allowed to access the pages that include these settings."
- MUST: "If a page is disallowed from crawling through the robots.txt file, then any information about indexing or serving rules will not be found and will therefore be ignored. If indexing or serving rules must be followed, the URLs containing those rules cannot be disallowed from crawling."
- Note: "Place the robots meta tag in the <head> section of a given page"; "Google Search doesn't enforce placement of meta robots in the HTML head and will respect robots meta tags in the body section".
- Note: "Both the name and the content attributes are case-insensitive." Google supports "googlebot" and "googlebot-news" as user agent tokens; "other values are ignored".
- MUST (non-HTML): "To block indexing of non-HTML resources, such as PDF files, video files, or image files, use the X-Robots-Tag response header instead."
- Conflict rule: "In the case of conflicting robots rules, the more restrictive rule applies."
- Rules: "all" (default); "noindex" ("Do not show this page, media, or resource in search results."); "nofollow"; "none" ("Equivalent to noindex, nofollow."); "nosnippet"; "indexifembedded" ("only has an effect if it's accompanied by noindex"); "max-snippet: [number]"; "max-image-preview: [setting]" (none, standard, large); "max-video-preview: [number]"; "notranslate"; "noimageindex"; "unavailable_after: [date/time]".
- Default if unset (snippet): "If you don't specify this rule, Google may generate a text snippet and video preview based on information found on the page."
- Default if unset (image): "If you don't specify the max-image-preview rule, Google may show an image preview of the default size."
- nosnippet scope: "This applies to all forms of search results (at Google: web search, Google Images, Discover, AI Overviews, AI Mode) and will also prevent the content from being used as a direct input for AI Overviews and AI Mode."
- max-snippet scope: "will also limit how much of the content may be used as a direct input for AI Overviews and AI Mode."
- max-snippet exception: "this limit does not apply in cases where a publisher has separately granted permission for use of content. For instance, if the publisher supplies content in the form of in-page structured data".
- Structured data: "Robots meta tag limitations don't affect the use of that structured data, with the exception of article.description"; "structured data remains usable for search results when declared within a data-nosnippet element."
- data-nosnippet: "on span, div, and section elements... the HTML section must be valid HTML and all appropriate tags must be closed accordingly." "do not add or remove the data-nosnippet attribute of existing nodes through JavaScript."
- Historical, ignored: "noarchive ... no longer used", "nocache isn't used", "nositelinkssearchbox ... no longer used".
- Multi-crawler: "the search engine will use the sum of the negative rules."
- unavailable_after: "Googlebot will decrease the crawl rate of the URL considerably after the specified date and time."
- Note (CMS): "If you use a CMS, such as Wix, WordPress, or Blogger, you might not be able to edit your HTML directly".
- N/A: Apache and NGINX X-Robots-Tag server config examples apply only if non-HTML files need rules; the googlebot-news token: the site is not in Google News.

## 17. Avoid intrusive interstitials and dialogs
URL: https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials  | Fetched: 2026-10-10 | Page says "Last updated 2025-12-10 UTC" | File: avoid-intrusive-interstitials.txt

- Definition: "Interstitials are overlays on the whole page and dialogs are overlays only on a part of the page, sometimes also obfuscating the underlying content."
- Consequence: "Intrusive dialogs and interstitials make it hard for Google and other search engines to understand your content, which may lead to poor search performance."
- SHOULD: "Instead of full page interstitials, use banners that take up only a small fraction of the screen to grab your users' attention."
- SHOULD: "You can reuse these small containers for other kinds of notifications, such as newsletter sign-up prompts."
- SHOULD: "Many CMSes have plugins that create standard dialogs and interstitials for the most common use cases, such as newsletter sign-up prompts." (the page then points WordPress users to plugin search)
- NEVER: "Don't obscure the entire page with interstitials."
- NEVER: "Don't redirect the user to a separate page for their consent or input."
- Exemption: "Unless they're legally mandatory". "Mandatory interstitials are exempted from the guidelines discussed in this document; however, if possible, we recommend that sites follow these best practices": overlay the content; "Don't redirect the incoming HTTP requests to a different page for collecting consent or providing data."
- N/A: age gates for adult content and Smart App Banners for app installs: the site publishes neither.

## 18. Core Web Vitals
URL: https://developers.google.com/search/docs/appearance/core-web-vitals  | Fetched: 2026-10-10 | Page says "Last updated 2025-12-10 UTC" | File: core-web-vitals.txt

- SHOULD: "We highly recommend site owners achieve good Core Web Vitals for success with Search and to ensure a great user experience generally."
- Note: "This, along with other page experience aspects, aligns with what our core ranking systems seek to reward."
- SHOULD: "Largest Contentful Paint (LCP)... strive to have LCP occur within the first 2.5 seconds of the page starting to load."
- SHOULD: "Interaction To Next Paint (INP)... strive to have an INP of less than 200 milliseconds."
- SHOULD: "Cumulative Layout Shift (CLS)... strive to have a CLS score of less than 0.1."
- SHOULD: "Check the Core Web Vitals report in Search Console."

## 19. Qualify outbound links
URL: https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links  | Fetched: 2026-10-10 | Page says "Last updated 2025-12-10 UTC" | File: qualify-outbound-links.txt

- Note: "For regular links that you expect Google to fetch and parse without any qualifications, you don't need to add a rel attribute."
- MUST (paid links, as the page words it): "Mark links that are advertisements or paid placements (commonly called paid links) with the sponsored value."
- Note: "The nofollow attribute was previously recommended for these types of links and is still an acceptable way to flag them, though sponsored is preferred."
- SHOULD: "We recommend marking user-generated content (UGC) links, such as comments and forum posts, with the ugc value."
- Option: "If you want to recognize and reward trustworthy contributors, you might remove this attribute from links posted by members or users who have consistently made high-quality contributions over time."
- Option: "Use the nofollow value when other values don't apply, and you'd rather Google not associate your site with, or crawl the linked page from, your site."
- Multiple values: "You may specify multiple rel values as a space- or comma-separated list."
- Note: "Links marked with these rel attributes will generally not be followed... the linked pages may be found through other means, such as sitemaps or links from other sites, and thus they may still be crawled."
- Right tool: "If you need to prevent Google from fetching a link to a page on your own site, use the robots.txt disallow rule." "To prevent Google from indexing a page, allow crawling and use the noindex robots rule."
- Note: the page does not use the word "affiliate"; the wording it uses is "advertisements or paid placements (commonly called paid links)".

## 20. Do you need an SEO?
URL: https://developers.google.com/search/docs/fundamentals/do-i-need-seo  | Fetched: 2026-10-10 (page exists) | Page says "Last updated 2026-06-05 UTC" | File: do-i-need-seo.txt

- Note: "Advertising with Google won't have any effect on your site's presence in our search results. Google never accepts money to include or rank sites in our search results, and it costs nothing to appear in our organic search results."
- Note: "If you run a small local business, you can probably do much of the work yourself. We recommend starting with the SEO starter guide".
- NEVER (when hiring): "No one can guarantee a #1 ranking on Google. Beware of SEOs that claim to guarantee rankings, allege a 'special relationship' with Google, or advertise a 'priority submit' to Google."
- NEVER: "If an SEO creates deceptive or misleading content on your behalf, your site could be removed entirely from Google's index. Ultimately, you are responsible for the actions of any companies you hire".
- NEVER: "You should never have to link to an SEO." "Avoid SEOs that talk about link popularity schemes or submitting your site to thousands of search engines."
- SHOULD: "If your SEO offers to do an SEO audit for you, be sure to carefully consider what's involved and only grant read access to Search Console (at this stage, don't grant them write access)."
- Note (tools): "Google doesn't evaluate or endorse third-party SEO tools, and these tools don't have access to Google's internal ranking data. Be wary of tools that claim to be 'acceptable' or 'approved' by Google Search."
- SHOULD: "Before making significant changes to your site based on a third-party tool's audit, be sure to check their recommendations against official guidance from Google Search".
- SHOULD: advice on AI experiences ("AEO" "GEO") should be checked: "is their advice aligned with Google Search's official guidance on optimizing for generative AI features?"
- Note: "some unethical SEOs have given the industry a black eye by using overly aggressive marketing efforts or using techniques that violate our spam policies, which may result in a negative adjustment of your site's presence in Google, or even the removal of your site from our index."
- N/A: reporting to the FTC or econsumer.gov applies only if an SEO deceives the owner.
