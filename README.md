# Pablo's Plugins

A central Codex marketplace for independently maintained plugins. This repository
contains the catalog and installation guide; plugin code stays in its own repo.
Entries are pinned to reviewed commits so installing from this catalog does not
silently follow development branches.

## Plugins

| Plugin | Version | Source package | Pinned commit |
|---|---|---|---|
| Universal Lever | 0.1.1 | [pablopoo/universal-lever](https://github.com/pablopoo/universal-lever/tree/ea612e63fadc82d16bd62d24062b1139b7fa4f88/plugins/universal-lever) | [`ea612e6`](https://github.com/pablopoo/universal-lever/commit/ea612e63fadc82d16bd62d24062b1139b7fa4f88) |
| GStack Power Team | 1.2.3 | [pablopoo/gstack-generic](https://github.com/pablopoo/gstack-generic/tree/75e58b7503701670a7f305c36f5b13bee3c25f7d/plugins/gstack-power-team) | [`75e58b7`](https://github.com/pablopoo/gstack-generic/commit/75e58b7503701670a7f305c36f5b13bee3c25f7d) |

Universal Lever provides one coordinator skill for measurement, experiments,
delivery and review. GStack Power Team provides curated product and engineering
methodologies with its own coordinator. Each plugin retains its own instructions,
license and release cycle. Combining them in a catalog does not merge their
instructions, create a permanent agent team, or require a specific model.

## Install in Codex

Use a Codex CLI that supports `plugin marketplace add` and `plugin add`:

```sh
codex plugin marketplace add pablopoo/codex-marketplace
codex plugin add universal-lever@pablopoo-plugins
codex plugin add gstack-power-team@pablopoo-plugins
```

The source repository is `pablopoo/codex-marketplace`; the catalog identifier is
`pablopoo-plugins`. Register the source once and install either or both plugins.
Adding the marketplace alone does not install them. Start a new Codex session
after installation, then ask it to use Universal Lever or GStack Power Team.

The full source URL also works:

```sh
codex plugin marketplace add https://github.com/pablopoo/codex-marketplace.git
```

The catalog and both plugin repositories are public. Reading these Git sources
does not require GitHub credentials. Workspace import may still require GitHub
authorization and workspace permissions. Publishing a repository on GitHub does
not automatically list its plugins in a public plugin directory.

## Codex / ChatGPT Desktop

Register the marketplace with the first command above on the computer and OS
user used by the desktop Codex environment, then restart the app. Open **Plugins**,
select **Pablo's Plugins**, and install either plugin. Skip the install action if
you already installed it with the CLI. Start a new conversation afterward.
These plugins target filesystem and shell workflows; use an appropriate Codex or
ChatGPT Work environment. Available controls depend on the app and workspace.

Eligible workspace admins can instead import the repository through **Admin
Console → Plugins → Add → Import marketplace**. Use Source
`https://github.com/pablopoo/codex-marketplace`, leave Path empty, select `main`,
and authorize GitHub access to the catalog and both plugin repositories. Review
workspace installation policies separately. See [official GitHub marketplace
import help](https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github).

## Existing installations

Marketplace identifiers are part of plugin selectors. An existing
`universal-lever@universal-lever` or `gstack-power-team@gstack-local` installation
is separate from the central catalog's installation. Review the installed version
and any local customizations before migrating. Disable or remove the old copy
when switching so both copies do not expose duplicate skills. This catalog does
not automatically migrate or uninstall anything.

Use the plugin table above to compare selected versions and commits. Do not
replace an existing newer local installation without comparing its changes; a
central catalog pin is not a claim that it is the latest version in development.

## Updates and maintenance

Plugin developers release changes in the plugin's own repository. To update the
catalog, review the exact new commit and package, run relevant validation, then
change its full `source.sha` and the version/commit table in this README. Preserve
package names and paths unless a migration is intentional. Never substitute a
floating `ref` for a reviewed pin.

Refresh the catalog source after its pins change:

```sh
codex plugin marketplace upgrade pablopoo-plugins
```

Refreshing a catalog is separate from replacing an installed cached plugin.
Review the available version in the plugin browser and refresh or reinstall it
using your client's supported controls, then start a new session. Workspace
admins can use **Sync now** for a GitHub-managed marketplace. Reinstalling while
the catalog pin is unchanged still selects the same plugin commit.

Validate the catalog locally:

```sh
python3 tests/validate.py
```

The check validates catalog structure, immutable source selectors and local
documentation links. It does not prove GitHub access or plugin behavior. Source
access and package discovery should also be checked before publishing pin updates.

See the [official marketplace format](https://developers.openai.com/plugins/build/plugins#marketplace-metadata)
and [plugin installation help](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt).

## License

This catalog is MIT licensed. Referenced plugins retain their own licenses and
upstream attribution in their source repositories and installed packages.
