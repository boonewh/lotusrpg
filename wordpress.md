# LOTUS Rulebook in WordPress (Bricks + PMPro) — Step-by-Step Guide

**Goal:** Recreate your current dynamic rulebook page in WordPress using Bricks 2.x, a Custom Post Type for rules, and Paid Memberships Pro (PMPro) to restrict access by level (Silver/Gold/Diamond).

## What you'll end up with

- A **Rules** content type (CPT) grouped by **Chapters** (taxonomy)
- A Bricks Single Rule template with a left sticky nav (query loop of rules) and right content
- Optional off-canvas nav on mobile
- PMPro membership levels with:
  - Entire posts/chapters restricted to paying members
  - Optional partial content restrictions inside a post
  - Clean URLs like `/rules/from-the-beginning`

## 1. Prerequisites

- WordPress installed
- Bricks Theme (2.x) active
- Admin access

## 2. Install & activate plugins

- **Paid Memberships Pro (PMPro)**
- **PMPro – Custom Post Type Membership Access** (official add-on)
- **Custom Post Type UI (CPT UI)** or plan to add the code below
- *(Optional, but recommended)* **Advanced Custom Fields (ACF)** if you want structured fields later

> **Note:** Nothing else required for AJAX pagination; Bricks query loop has "Load more" built in.

## 3. Create your content model

### Option A — Use CPT UI (fastest)

**CPT UI → Add/Edit Post Types**
- Post Type Slug: `rules`
- Plural Label: `Rules`
- Singular Label: `Rule`
- Enable Has Archive, Show in REST
- Rewrite slug: `rules`

**CPT UI → Add/Edit Taxonomies**
- Taxonomy Slug: `chapters`
- Plural: `Chapters`
- Singular: `Chapter`
- Attach to Post Type: `rules`
- Hierarchical: `Yes`

### Option B — Code (put in a small mu-plugin or child theme functions.php)

Create `/wp-content/mu-plugins/lotus-cpt.php` (create the mu-plugins folder if needed):

```php
<?php
/**
 * Plugin Name: LOTUS CPT
 */
add_action('init', function () {
    register_post_type('rules', [
        'labels' => ['name' => 'Rules', 'singular_name' => 'Rule'],
        'public' => true,
        'has_archive' => true,
        'show_in_rest' => true,
        'rewrite' => ['slug' => 'rules'],
        'supports' => ['title','editor','excerpt','thumbnail','revisions'],
        'menu_position' => 21,
        'menu_icon' => 'dashicons-book-alt',
    ]);

    register_taxonomy('chapters', 'rules', [
        'labels' => ['name' => 'Chapters', 'singular_name' => 'Chapter'],
        'hierarchical' => true,
        'public' => true,
        'show_in_rest' => true,
        'rewrite' => ['slug' => 'chapters'],
    ]);
});
```

## 4. Add membership levels in PMPro

**Memberships → Settings → Levels → Add New**

1. **Free** (ID 1, typically) — no access to premium content
2. **Silver**
3. **Gold**
4. **Diamond**

> **Note:** Note the numeric IDs (you'll need them for shortcodes). Hover the level title to see the ID or check the URL.

## 5. Enable CPT protection for Rules

1. Activate **PMPro – Custom Post Type Membership Access** add-on
2. Edit any Rule post:
   - Find the **Require Membership** metabox
   - Check Silver, Gold, Diamond to require one of those levels to view that post
3. **Memberships → Settings → Advanced**
   - Turn **ON** Filter searches and archives so restricted rules don't appear to non-members in loops

> **Note:** If "Rules" doesn't get filtered by default, add the tiny snippet in section 10.2.

## 6. Create Bricks templates
### 6.1 Archive: Rules (optional but nice)

Bricks → Templates → Add New → Archive

Template Conditions: Post Type Archive → rules

Layout:

Section → Container

Heading: “Rules”

Query Loop (Element → Posts) targeting rules

Card content: title, excerpt, link

Enable Pagination or Load More (AJAX)

### 6.2 Single: Rule (the main page)

Bricks → Templates → Add New → Single

Template Conditions: Single → Post Type = rules

Layout (desktop):

Section (max width 1200–1400px)

Container (display: grid; columns 320px 1fr; gap: 2rem)

Left column (nav)

Container (width 100%; set Position: sticky; Top: 1rem)

Heading: “Chapters”

Query Loop (Element → Posts or Terms)

Option A (flat list of rules): Query rules, order by title or menu_order.

Option B (grouped by chapters):

Outer Query Loop → terms of chapters

Inner Query Loop → rules filtered by current term

Output: anchor links to each rule permalink

Add Active state: compare current post ID with loop item (see 10.1)

Right column (content)

Post Title

Post Content

Optional “Next/Previous rule” links (Bricks Dynamic Data → Next/Prev post)

Mobile

Hide the left column at the tablet/phone breakpoints.

Add a Button in the header: “Chapters”

Add Off-canvas element containing the same Query Loop from the left nav.

Toggle the off-canvas with the button.

## 7. Make the left nav load like your old dynamic page

If the list is very long, select the **Query Loop → Pagination → Load More (AJAX)**.

This keeps users on the page while extending the list (no full refresh).

> **Note:** For true PJAX (replace main content without page reload), you'd need a custom solution; in most cases normal page navigation + sticky nav is simpler and SEO-friendly.

## 8. Add/Import your content

**Chapters (taxonomy):** create terms like Introduction, Character Genesis, etc.

**Rules (CPT):**
- Create a post for each rule page
- Assign the right Chapter term
- Paste your content (use headings `<h2>…</h2>`, paragraphs, images as needed)

***(Optional)* If migrating a lot:**
- Use **WP All Import** to import a CSV of rules mapping title/content/chapter

## 9. Restrict entire posts vs. partial content
### 9.1 Entire posts

- On each Rule, check **Require Membership → Silver/Gold/Diamond**
- Non-members see the PMPro message (customize in PMPro settings/templates)

### 9.2 Partial content (inside a rule)

Wrap premium sections with the PMPro shortcode using your level IDs:

```shortcode
[membership level="2,3,4"]
<p>Premium section visible only to Silver, Gold, Diamond.</p>
[/membership]

[membership level="!2,!3,!4"]
<p>Upsell or teaser for non-members/free.</p>
[/membership]
```

> **Note:** `!` means "not this level." Use IDs that match your levels.

## 10. Helpful snippets (optional but recommended)
### 10.1 Mark the active rule in the left nav

In the Query Loop template for nav items, add a class condition using Bricks conditions:

For the Link element, set a dynamic Class like:
- **Base class:** `nav-link`
- **Conditional class:** `is-active` when `{post_id}` equals `{current_post_id}` (Bricks dynamic tags)

**Minimal CSS:**
```css
.nav-link { 
    display: block; 
    padding: .4rem .6rem; 
    border-radius: .4rem; 
}
.nav-link.is-active { 
    font-weight: 700; 
    text-decoration: underline; 
}
```

### 10.2 Ensure PMPro hides restricted Rules in all queries

If you see restricted Rules still appearing in lists, add this:

```php
// Include 'rules' CPT in PMPro archive/search filtering
add_filter('pmpro_search_filter_post_types', function($post_types) {
    if (!in_array('rules', $post_types, true)) {
        $post_types[] = 'rules';
    }
    return $post_types;
});
```

### 10.3 Make the left nav sticky

Set CSS on the left column container:

```css
.lotus-nav {
    position: sticky;
    top: 1rem;       /* adjust for your header height */
    max-height: calc(100vh - 2rem);
    overflow: auto;
}
```

Add `lotus-nav` to that container's CSS class in Bricks.

## 11. SEO & UX touches

- **Permalink structure:** Settings → Permalinks → Post name. Your CPT uses `/rules/%postname%/`
- **Breadcrumbs:** optional (Yoast or RankMath). Place above the Post Title
- **Meta/Schema:** your Rules template can output unique meta—your earlier SEO goal benefits from titles/excerpts per rule
- **Scroll to top / in-page TOC:** optional for long rules

## 12. Testing checklist

- [ ] **As a guest:** only public/free rules appear in archive/nav; protected singles show PMPro message
- [ ] **As Free member:** same as guest unless you explicitly grant access to some free content
- [ ] **As Silver/Gold/Diamond:** can view all restricted rules and premium sections
- [ ] **Mobile:** off-canvas opens, list scrolls, page content navigates cleanly
- [ ] **Performance:** long nav lists paginate with Load More; sticky works; no layout shifts

## 13. Migration tips from your old site

- Keep slugs consistent to preserve URLs (e.g., `from-the-beginning`)
- If the old site used a different structure, add **Redirections** (plugin) from old paths to new ones
- Bring over images to the Media Library and update references

## 14. What to do next (order of operations)

1. Install plugins (PMPro + CPT add-on + CPT UI)
2. Create Rules CPT & Chapters taxonomy
3. Add membership levels
4. Build Single: Rule Bricks template (columns, sticky nav query loop, content)
5. *(Optional)* Build Archive: Rules template
6. Add a few Chapters and Rules as test content
7. Apply Require Membership on a couple of posts and wrap a section with `[membership]`
8. Turn on Filter searches and archives; add snippet 10.2 if needed
9. Style the nav; add off-canvas for mobile
10. Test as guest, Free, and paid members

## 15. Optional enhancements

- **Chapter index page** that lists chapters with counts
- **Next/Previous navigation** at the bottom of singles
- **Custom upsell block** for non-members on restricted posts
- **ACF fields** for stat blocks or rule metadata; display via Bricks dynamic data

---

### If you want, I can:

- Generate a starter Bricks Single template structure (element tree + settings)
- Provide a CSV template to bulk-import your rules with chapters
- Or paste a ready-to-drop mu-plugin containing the CPT, taxonomy, and PMPro filter