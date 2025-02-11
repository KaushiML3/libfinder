    publish:
        name : Publish Python distribution
        runs-on: ubuntu-18.04
        needs: python-build
        if: github.event_name == 'release'
        steps:
            - name: Download a distribution artifact
              uses: actions/download-artifact@v2
              with:
                name: dist-package-3.9
                path: dist
    
            - name: Publish distribution 📦 to Test PyPI
              uses: pypa/gh-action-pypi-publish@master
              with:
                skip_existing: true
                user: __token__
                password: ${{ secrets.pypi_libfinder_test }}
                repository_url: https://test.pypi.org/legacy/
    
            - name: Publish distribution 📦 to PyPI
              uses: pypa/gh-action-pypi-publish@master
              with:
                user: __token__
                password: ${{ secrets.pypi_libfinder }}