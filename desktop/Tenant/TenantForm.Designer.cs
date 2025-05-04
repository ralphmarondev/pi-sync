namespace PiSync.Tenant
{
    partial class TenantForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            btnNewTenant = new Button();
            label2 = new Label();
            tbSearch = new TextBox();
            lblTitle = new Label();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.MediumPurple;
            panel1.Controls.Add(btnNewTenant);
            panel1.Controls.Add(label2);
            panel1.Controls.Add(tbSearch);
            panel1.Controls.Add(lblTitle);
            panel1.Dock = DockStyle.Top;
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(875, 79);
            panel1.TabIndex = 0;
            // 
            // btnNewTenant
            // 
            btnNewTenant.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnNewTenant.BackColor = Color.Lavender;
            btnNewTenant.FlatAppearance.BorderSize = 0;
            btnNewTenant.FlatStyle = FlatStyle.Flat;
            btnNewTenant.Location = new Point(729, 24);
            btnNewTenant.Name = "btnNewTenant";
            btnNewTenant.Size = new Size(121, 43);
            btnNewTenant.TabIndex = 10;
            btnNewTenant.Text = "NEW";
            btnNewTenant.UseVisualStyleBackColor = false;
            // 
            // label2
            // 
            label2.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            label2.AutoSize = true;
            label2.Font = new Font("Courier New", 10F);
            label2.ForeColor = Color.Lavender;
            label2.Location = new Point(490, 9);
            label2.Name = "label2";
            label2.Size = new Size(169, 20);
            label2.TabIndex = 9;
            label2.Text = "TENANT USERNAME:";
            // 
            // tbSearch
            // 
            tbSearch.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            tbSearch.BackColor = Color.Lavender;
            tbSearch.Location = new Point(490, 32);
            tbSearch.Name = "tbSearch";
            tbSearch.Size = new Size(225, 30);
            tbSearch.TabIndex = 8;
            // 
            // lblTitle
            // 
            lblTitle.AutoSize = true;
            lblTitle.Font = new Font("Courier New", 16F);
            lblTitle.ForeColor = Color.Lavender;
            lblTitle.Location = new Point(59, 24);
            lblTitle.Margin = new Padding(5, 0, 5, 0);
            lblTitle.Name = "lblTitle";
            lblTitle.Size = new Size(125, 30);
            lblTitle.TabIndex = 2;
            lblTitle.Text = "TENANTS";
            // 
            // TenantForm
            // 
            AutoScaleDimensions = new SizeF(12F, 22F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(875, 520);
            Controls.Add(panel1);
            Font = new Font("Courier New", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(4, 3, 4, 3);
            Name = "TenantForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "TenantForm";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Label lblTitle;
        private Label label2;
        private TextBox tbSearch;
        private Button btnNewTenant;
    }
}