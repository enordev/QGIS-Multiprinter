# Get the layout manager from the current project
manager = QgsProject.instance().layoutManager()

# Loop through all print layouts in the project
for layout in manager.printLayouts():
    print("Exporting layout:", layout.name())

    # Create an exporter for the current layout
    exporter = QgsLayoutExporter(layout)

    # Define the output file path (use raw string to avoid backslash issues)
    output_path = rf"D:\temp\{layout.name()}.pdf"

    # Export to PDF
    result = exporter.exportToPdf(output_path, QgsLayoutExporter.PdfExportSettings())

    if result == QgsLayoutExporter.Success:
        print(f"Successfully exported {layout.name()} to {output_path}")
    else:
        print(f"Failed to export {layout.name()}")
